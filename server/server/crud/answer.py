import logging
from typing import List

from fastapi import HTTPException
from server.core.models import Answer, Answer2Label
from server.core.schemas import AnswerCreate, AnswerUpdate
from server.crud.base import CRUDBase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from .label import label_crud

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    
    def get(self, db: Session, id: int) -> Answer | None:
        logging.info(f"CRUDAnswer: Start query with id\={id}")
        try:
            answer = db.query(self.model).options(joinedload(self.model.labels).options(joinedload(Answer2Label.label_obj)))\
                .filter(self.model.id == id).first()
                
            logging.info(f"CRUDAnswer: End query with id\={id}: Successful")
            return answer
        except SQLAlchemyError:
            logging.error(f"CRUDAnswer: End query with id\={id}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 1000000
    ) -> List[Answer]:
        logging.info(f"CRUDAnswer: Start multiple query")
        try:
            answers = db.query(self.model)\
                    .options(joinedload(self.model.labels).options(joinedload(Answer2Label.label_obj)))\
                    .offset(skip)\
                    .limit(limit)\
                    .all()
                    
            logging.info(f"CRUDAnswer: End multiple query: Successful")
            return answers
        except SQLAlchemyError:
            logging.error(f"CRUDAnswer: End multiple query: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")
    
    def create(self, db: Session, *, answer_schema: AnswerCreate) -> Answer:
        logging.info(f"CRUDAnswer: Start create answer with schema\={answer_schema}")
        answer = Answer(
            description=answer_schema.description,
            question_id=answer_schema.question_id
        )
        try:
            db.add(answer)
            db.flush()
        except SQLAlchemyError:
            logging.error(f"CRUDAnswer: End create answer with schema\={answer_schema}: Error", exc_info=True)
            db.rollback()
            raise HTTPException(status_code=500, detail=f"{type(self).__name__} Error at adding in the database")
        
        for label_info in answer_schema.labels:
            db_label = label_crud.get_by_label(db=db, label=label_info.label)
            answer2label = Answer2Label(
                answer_id=answer.id,
                label_id=db_label.id,
                score=label_info.score
            )
            try:
                db.add(answer2label)
            except SQLAlchemyError:
                logging.error(f"CRUDAnswer: End create answer with schema\={answer_schema}: Error", exc_info=True)
                db.rollback()
                raise HTTPException(status_code=500, detail=f"{type(self).__name__} Error at adding in the database")
        
        try:
            db.commit()
            db.refresh(answer)
        except SQLAlchemyError:
            db.rollback()
            logging.error(f"CRUDAnswer: End create answer with schema\={answer_schema}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__} Error at committing the database")
        
        logging.info(f"CRUDAnswer: End create answer with schema\={answer_schema}: Successful")
        return answer

answer_crud = CRUDAnswer(Answer)
