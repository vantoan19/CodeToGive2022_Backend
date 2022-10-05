from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import answer_crud, submit_answer
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.AnswerWithLabels])
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

@router.put("/{answer_id}", response_model=schemas.AnswerWithLabels)
def update_answer(
    *,
    db: Session = Depends(get_db),
    answer_id: int,
    answer_info: schemas.AnswerUpdate
) -> Any:
    answer_db = answer_crud.get(db=db, id=answer_id)
    if not answer_db:
        raise HTTPException(status_code=404, detail="answer not found")
    answer = answer_crud.update(db=db, db_obj=answer_db, obj_in=answer_info)
    return answer
