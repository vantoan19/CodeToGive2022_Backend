import logging
from typing import Any, Dict, List

from fastapi import HTTPException
from server.core.models import QuestionType, Test, Test2Question, TestType
from server.core.schemas.test import TestCreate, TestUpdate
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from .base import CRUDBase
from .crud_exception import NotImplementedException
from .question import question_crud

logging.basicConfig(level=logging.DEBUG, format="%(process)d-%(levelname)s-%(message)s")

test_type_to_question_type = {
    TestType.ENGLISH_TEST: QuestionType.ENGLISH_QUESTION,
    TestType.MOTIVATION_TEST: QuestionType.MOTIVATION_QUESTION,
    TestType.SOCIAL_SITUATION_TEST: QuestionType.SOCIAL_SITUATION_QUESTION,
    TestType.VISIO_PERCEPTUAL_TEST: QuestionType.VISIO_PERCEPTUAL_QUESTION,
}

test_titles = {
    TestType.ENGLISH_TEST: "English test",
    TestType.MOTIVATION_TEST: "Work motivation test",
    TestType.SOCIAL_SITUATION_TEST: "Interpretation of Social Situations test",
    TestType.VISIO_PERCEPTUAL_TEST: "Measurement of Visio-perceptual abilities test",
}


class CRUDTest(CRUDBase[Test, TestCreate, TestUpdate]):
    def get(self, db: Session, id: int) -> Test | None:
        logging.info(f"CRUDAnswer: Start query with id\={id}")
        try:
            test = (
                db.query(self.model)
                .options(
                    joinedload(self.model.questions).options(
                        joinedload(Test2Question.question)
                    )
                )
                .filter(self.model.id == id)
                .first()
            )

            logging.info(f"CRUDAnswer: End query with id\={id}: Successful")
            return test
        except SQLAlchemyError:
            logging.error(f"CRUDAnswer: End query with id\={id}: Error", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail=f"{type(self).__name__}: Error at querying the database",
            )

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 1000000
    ) -> List[Test]:
        logging.info(f"CRUDAnswer: Start multiple query")
        try:
            test = (
                db.query(self.model)
                .options(
                    joinedload(self.model.questions).options(
                        joinedload(Test2Question.question)
                    )
                )
                .offset(skip)
                .limit(limit)
                .all()
            )

            logging.info(f"CRUDAnswer: End multiple query: Successful")
            return test
        except SQLAlchemyError:
            logging.error(f"CRUDAnswer: End multiple query: Error", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail=f"{type(self).__name__}: Error at querying the database",
            )

    def get_test_of_an_assessment(
        self, db: Session, test_type: TestType, uuid: str
    ) -> Test | None:
        logging.info(
            f"{type(self).__name__}: Start get test of assessment uuid\={uuid}"
        )
        try:
            test = (
                db.query(self.model)
                .filter(self.model.assessment_uuid == uuid)
                .filter(self.model.type == test_type)
                .first()
            )
            logging.info(
                f"{type(self).__name__}: End get test of assessment uuid\={uuid}: Successful"
            )
            return test
        except SQLAlchemyError:
            logging.error(
                f"{type(self).__name__}: End get test of assessment uuid\={uuid}: Error",
                exc_info=True,
            )
            raise HTTPException(
                status_code=500,
                detail=f"{type(self).__name__}: Error at querying the database",
            )

    def update(
        self, db: Session, *, db_obj: Test, obj_in: TestUpdate | Dict[str, Any]
    ) -> Test:
        raise NotImplementedException(crud_component="Test", crud_operation="Update")

    def generate_test(self, db: Session, test_info: TestCreate) -> Test:
        logging.info(f"{type(self).__name__}: Start generate test")

        try:
            questions = question_crud.get_by_type_randomly(
                db=db, limit=5, question_type=test_type_to_question_type[test_info.type]
            )
        except Exception as e:
            logging.error(
                f"{type(self).__name__}: End generate test: Error", exc_info=True
            )
            raise e
        try:
            test = Test(
                assessment_uuid=test_info.assessment_uuid,
                type=test_info.type,
                title=test_titles[test_info.type],
                description=test_info.description,
            )
            db.add(test)
            db.flush()
            for question in questions:
                test2question = Test2Question(question_id=question.id, test_id=test.id)
                db.add(test2question)
                db.flush()
        except SQLAlchemyError:
            logging.error(
                f"{type(self).__name__}: End generate test: Error", exc_info=True
            )
            raise HTTPException(
                status_code=500,
                detail=f"{type(self).__name__}: Error at adding the database",
            )

        try:
            db.commit()
            db.refresh(test)
        except SQLAlchemyError:
            logging.error(
                f"{type(self).__name__}: End generate test: Error", exc_info=True
            )
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"{type(self).__name__}: Error at committing the database",
            )
        logging.info(f"{type(self).__name__}: End generate test: Successful")
        return test


test_crud = CRUDTest(Test)
