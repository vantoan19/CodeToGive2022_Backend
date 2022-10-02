from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import assessment_crud, test_crud
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{assessment_uuid}", response_model=schemas.Assessment)
def read_assessment_by_uuid(
    *,
    db: Session = Depends(get_db),
    assessment_uuid: str
) -> Any:
    assessment = assessment_crud.get_by_uuid(db, uuid=assessment_uuid)
    return assessment

@router.get("/", response_model=List[schemas.Assessment])
def read_assessments(
    db: Session = Depends(get_db)
) -> Any:
    assessments = assessment_crud.get_multi(db=db)
    return assessments

@router.get("/{assessment_uuid}/tests", response_model=schemas.Test)
def read_work_motivation_test_for_an_assessment_by_uuid(
    *,
    db: Session = Depends(get_db),
    assessment_uuid: str,
    test_type: models.TestType
) -> Any:
    test = test_crud.get_test_of_an_assessment(db=db, test_type=test_type, uuid=assessment_uuid)
    return test

@router.post("/generate", response_model=schemas.Assessment)
def generate_assessment(
    db: Session = Depends(get_db)
) -> Any:
    assessment = assessment_crud.generate_assessment(db=db)
    return assessment
