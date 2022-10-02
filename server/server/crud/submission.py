import logging
from typing import Any

from fastapi import HTTPException
from server.core import models, schemas
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

def submit_answer(db: Session,answer_info: schemas.AnswerSubmit) -> Any:
    logging.info(f"CRUDSubmission: Start submit an answer with schema\={answer_info}")
    test2question = db.query(models.Test2Question)\
        .filter(models.Test2Question.test_id == answer_info.test_id)\
        .filter(models.Test2Question.question_id == answer_info.question_id)\
        .first()
    if not is_answer_belong_to_question(db, answer_info.answer_id, answer_info.question_id):
        raise HTTPException(status_code=406, detail=f"answer_id is not belong to the given question")
    test2question.answered_id = answer_info.answer_id
    
    try: 
        db.add(test2question)
        db.commit()
        db.refresh(test2question)
        
        logging.info(f"CRUDSubmission: End submit an answer with schema\={answer_info}: Successful")
        return {
            "message": "Submited the answer successfully"
        }
    except SQLAlchemyError:
        logging.error(f"CRUDSubmission: End submit an answer with schema\={answer_info}: Error", exc_info=True)
        raise HTTPException(status_code=500, detail=f"CRUDSubmission: Error at committing the database")

def is_answer_belong_to_question(db: Session, answer_id: int, question_id: int) -> bool:
    question = db.query(models.Question)\
        .filter(models.Question.id == question_id)\
        .first()   
    if answer_id not in map(lambda ans: ans.id, question.answers):
        return False
    return True
