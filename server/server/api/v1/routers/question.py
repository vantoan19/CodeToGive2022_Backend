from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import question_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{question_id}", response_model=schemas.Question)
def read_question(
    *,
    db: Session = Depends(get_db),
    question_id: int,
) -> Any:
    question = question_crud.get(db=db, id=question_id)
    return question

@router.get("/", response_model=List[schemas.Question])
def read_all_questions(
    db: Session = Depends(get_db)
) -> Any:
    questions = question_crud.get_multi(db=db)
    return questions

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
        answers=answers
    )
    question = question_crud.create(db=db, question_schema=create_schema)
    return question