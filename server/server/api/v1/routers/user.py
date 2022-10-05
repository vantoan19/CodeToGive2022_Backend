from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import user_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.User, response_model_exclude={"address": {"id", "user_id"}})
def read_user(
    *,
    db: Session = Depends(get_db),
    id: int
) -> Any:
    user = user_crud.get(db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.get("/", response_model=List[schemas.User], response_model_exclude={"address": {"id", "user_id"}})
def read_all_users(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10000000
) -> Any:
    users = user_crud.get_multi(db=db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=schemas.User, response_model_exclude={"address": {"id", "user_id"}})
def create_user(
    *,
    db: Session = Depends(get_db),
    user_info: schemas.UserCreate
) -> Any:
    user = user_crud.create(db=db, user_info=user_info)
    return user
