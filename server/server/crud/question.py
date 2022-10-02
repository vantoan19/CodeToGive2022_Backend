import logging
from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from server.core.models.question import Question, QuestionType
from server.core.schemas.answer import AnswerCreate
from server.core.schemas.question import QuestionCreate, QuestionUpdate
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql.expression import func

from .answer import answer_crud
from .base import CRUDBase

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    
    def get_by_type_randomly(self, db: Session, *, limit: int = 20, question_type: QuestionType) -> List[Question]:
        logging.info(f"{type(self).__name__}: Start get randomly with type\={question_type}")
        try:
            questions = db.query(self.model)\
                .filter(self.model.type == question_type)\
                .order_by(func.rand()).limit(limit).all()
                
            logging.info(f"{type(self).__name__}: End get randomly with type\={question_type}: Successful")
            return questions
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End get randomly with type\={question_type}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")
    
    def create(self, db: Session, *, question_schema: QuestionCreate) -> Question:
        logging.info(f"{type(self).__name__}: Start create with schema\={question_schema}")
        question = Question(
            type=question_schema.type,
            description=question_schema.description,
            img_url=question_schema.img_url,
            img_alt=question_schema.img_alt
        )
        try:
            db.add(question)
            db.flush()
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End create with schema\={question_schema}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at adding the database")
        
        
        for answer_info in question_schema.answers:
            try:
                answer_schema = AnswerCreate(**jsonable_encoder(answer_info), question_id=question.id)
                answer_crud.create(db=db, answer_schema=answer_schema)
            except Exception as e:
                logging.error(f"{type(self).__name__}: End create with schema\={question_schema}: Error", exc_info=True)
                raise e
        db.refresh(question)
        
        logging.info(f"{type(self).__name__}: End create with schema\={question_schema}: Successful")
        return question
            
question_crud = CRUDQuestion(Question)
