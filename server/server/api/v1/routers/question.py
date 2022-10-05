import logging
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import question_crud
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

router = APIRouter()

@router.get("/", response_model=List[schemas.QuestionWithLabels])
def read_all_questions(
    db: Session = Depends(get_db),
    skip: int = 0, 
    limit: int = 1000000,
    type: models.QuestionType = None,
) -> Any:
    questions = question_crud.get_multi(db=db, skip=skip, limit=limit)
    if type:
        questions = list(filter(lambda question: question.type == type ,questions))
    return questions

@router.get("/{question_id}", response_model=Optional[schemas.Question])
def read_question(
    *,
    db: Session = Depends(get_db),
    question_id: int,
) -> Any:
    question = question_crud.get(db=db, id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="question not found")
    return question

@router.post("/", response_model=schemas.Question)
def create_question(
    *,
    db: Session = Depends(get_db),
    question_info: schemas.QuestionCreate
) -> Any:
    question = question_crud.create(db=db, question_schema=question_info)
    return question

@router.post("/motivation-question", response_model=schemas.Question)
def create_motivation_question(
    *,
    db: Session = Depends(get_db),
    question_info: schemas.MotivationQuestionCreate
) -> Any:
    answers = [
        {
            "description": f"{score}",
            "labels": [
                {
                    "label": label,
                    "score": score
                }
                for label in question_info.labels
            ]
        } 
        for score in range(1, 6)
    ]
    create_schema = schemas.QuestionCreate(
        type=question_info.type,
        description=question_info.description,
        answers=answers,
        img_url=question_info.img_url,
        img_alt=question_info.img_alt
    )
    question = question_crud.create(db=db, question_schema=create_schema)
    return question

@router.put("/{question_id}", response_model=schemas.Question)
def update_question(
    *,
    db: Session = Depends(get_db),
    question_id: int,
    question_info: schemas.QuestionUpdate
):
    question = question_crud.get(db=db, id=question_id)
    question = question_crud.update(db=db, db_obj=question, obj_in=question_info)
    return question

@router.delete("/{question_id}")
def delete_a_question(
    *,
    db: Session = Depends(get_db),
    question_id: int
):
    question_crud.remove(db=db, id=question_id)
    return {
        "message": "Deleted the question successfully"
    }
    