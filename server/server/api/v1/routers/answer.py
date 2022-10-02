from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import answer_crud, submit_answer
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Answer])
def read_all_answers(
    db: Session = Depends(get_db),
) -> Any:
    answers = answer_crud.get_multi(db=db)
    return answers

@router.put("/submit")
def submit_single_answer(
    *,
    db: Session = Depends(get_db),
    answer_info: schemas.AnswerSubmit
) -> Any:
    return submit_answer(db, answer_info)
