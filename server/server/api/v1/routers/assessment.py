from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import assessment_crud, test_crud, user_crud
from sqlalchemy.orm import Session
from server.lib.job_suggestion import (
    get_suggestion_jobs_for_assessment,
    get_assessment_report,
)

router = APIRouter()


@router.get("/{assessment_uuid}", response_model=schemas.Assessment)
def read_assessment_by_uuid(
    *, db: Session = Depends(get_db), assessment_uuid: str
) -> Any:
    assessment = assessment_crud.get_by_uuid(db, uuid=assessment_uuid)
    if not assessment:
        raise HTTPException(status_code=404, detail="assessment not found")
    return assessment


@router.get("/", response_model=List[schemas.Assessment])
def read_assessments(db: Session = Depends(get_db)) -> Any:
    assessments = assessment_crud.get_multi(db=db)
    return assessments


@router.get("/{assessment_uuid}/tests", response_model=schemas.Test)
def read_work_motivation_test_for_an_assessment_by_uuid(
    *, db: Session = Depends(get_db), assessment_uuid: str, test_type: models.TestType
) -> Any:
    test = test_crud.get_test_of_an_assessment(
        db=db, test_type=test_type, uuid=assessment_uuid
    )
    if not test:
        raise HTTPException(status_code=404, detail="test not found")
    return test


@router.post("/", response_model=schemas.AssessmentWithOnlyUuid)
def create_assessment(db: Session = Depends(get_db)) -> Any:
    assessment = assessment_crud.create(db=db)
    return assessment


@router.post(
    "/generate",
    response_model=schemas.Assessment,
    response_model_exclude={"tests": {"__all__": {"questions"}}},
)
def generate_assessment(db: Session = Depends(get_db)) -> Any:
    assessment = assessment_crud.generate_assessment(db=db)
    return assessment


@router.put("/submit")
def submit_assessment(
    *, db: Session = Depends(get_db), submit_info: schemas.AssessmentSubmit
) -> Any:
    assessment = assessment_crud.get_by_uuid(db=db, uuid=submit_info.uuid)
    if assessment is None:
        raise HTTPException(status_code=404, detail="assessment not found")
    user_info = schemas.UserCreate(
        email=submit_info.email,
        first_name=submit_info.first_name,
        last_name=submit_info.last_name,
        phone_number=submit_info.phone_number,
    )
    user = user_crud.create(db=db, user_info=user_info)
    assessment_update_info = schemas.AssessmentUpdate(owner_id=user.id)
    assessment = assessment_crud.get_by_uuid(db=db, uuid=submit_info.uuid)
    return assessment_crud.update(
        db=db, db_obj=assessment, obj_in=assessment_update_info
    )


@router.get("/{uuid}/suggested-jobs", response_model=List[schemas.Job])
def get_suggested_jobs(*, db: Session = Depends(get_db), uuid: str) -> Any:
    result = get_suggestion_jobs_for_assessment(db, uuid=uuid)
    return result


@router.get("/{uuid}/report", response_model=List[schemas.LabelWithTotalScore])
def get_report(*, db: Session = Depends(get_db), uuid: str):
    return get_assessment_report(db=db, uuid=uuid)
