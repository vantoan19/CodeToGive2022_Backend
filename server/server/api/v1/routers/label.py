from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import label_crud
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Label])
def read_all_labels(
    db: Session = Depends(get_db)
) -> Any:
    labels = label_crud.get_multi(db=db)
    return labels

@router.get("/id/{label_id}", response_model=schemas.Label)
def read_label_by_id(
    *,
    db: Session = Depends(get_db),
    label_id: int
) -> Any:
    label = label_crud.get(db=db, id=label_id)
    if not label:
        raise HTTPException(status_code=404, detail="Label's id doesn't exist")
    return label

@router.get("/label/{label}", response_model=schemas.Label)
def read_label_by_label(
    *,
    db: Session = Depends(get_db),
    label: str
) -> Any:
    label = label_crud.get_by_label(db=db, label=label)
    if not label:
        raise HTTPException(status_code=404, detail="Label doesn't exist")
    return label

@router.post("/", response_model=schemas.Label)
def create_label(
    *,
    db: Session = Depends(get_db),
    label_schema: schemas.LabelCreate
) -> Any:
    label = label_crud.create(db=db, obj_in=label_schema)
    return label
