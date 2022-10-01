from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import user_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{id}", response_model=schemas.User)
def read_user(
    db: Session = Depends(get_db),
) -> Any:
    user = user_crud.get(db, id=id)
    return user

