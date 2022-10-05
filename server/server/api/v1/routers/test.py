from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import test_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{test_id}", response_model=schemas.Test)
def read_test(
    *,
    db: Session = Depends(get_db),
    test_id: int
) -> Any:
    test = test_crud.get(db=db, id=test_id)
    if not test:
        raise HTTPException(status_code=404, detail="test not found")
    return test

@router.get("/", response_model=List[schemas.Test])
def read_all_tests(
    db: Session = Depends(get_db)
) -> Any:
    tests = test_crud.get_multi(db=db)
    return tests

@router.post("/", response_model=schemas.Test)
def generate_test(
    *,
    db: Session = Depends(get_db),
    test_info: schemas.TestCreate
):
    test = test_crud.generate_test(db=db, test_info=test_info)
    return test
