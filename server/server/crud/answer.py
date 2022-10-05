import logging
from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
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
            if not db_label:
                raise HTTPException(status_code=404, detail=f"Given label {label_info.label} not found")
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
    
    def update(self, db: Session, db_obj: Answer, obj_in: AnswerUpdate) -> Answer:
        logging.info(f"{type(self).__name__}: Start updating with schema\={obj_in}")
        update_data = obj_in.dict(exclude_unset=True)
        obj_data = jsonable_encoder(db_obj)
        if "labels" in update_data:
            remove_all_answer2label_for_an_answer(db, db_obj.id)
            del db_obj.labels
            for label_info in update_data["labels"]:
                db_label = label_crud.get_by_label(db=db, label=label_info["label"])
                if not db_label:
                    raise HTTPException(status_code=404, detail=f"Given label {label_info.label} not found")
                answer2label = Answer2Label(
                    answer_id=db_obj.id,
                    label_id=db_label.id,
                    score=label_info["score"]
                )
                try:
                    db.add(answer2label)
                except SQLAlchemyError:
                    logging.error(f"CRUDAnswer: End updating answer with schema\={obj_in}: Error", exc_info=True)
                    db.rollback()
                    raise HTTPException(status_code=500, detail=f"{type(self).__name__} Error at adding in the database")
        for field in obj_data:
            if field is not "labels" and field in update_data:
                setattr(db_obj, field, update_data[field])
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            
            logging.info(f"{type(self).__name__}: End updating with schema\={obj_in}: Successful")
            return db_obj
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End updating with schema\={obj_in}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at committing in the database")
        
    
    
def remove_all_answer2label_for_an_answer(db: Session, answer_id: int):
    ans2labels = db.query(Answer2Label).filter(Answer2Label.answer_id == answer_id).all()
    for ans2label in ans2labels:
        db.delete(ans2label)
        db.flush()

answer_crud = CRUDAnswer(Answer)
