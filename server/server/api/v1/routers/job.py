from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from server.api.deps import get_db
from server.core import models, schemas
from server.crud import job_crud
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{id}", response_model=schemas.Job, response_model_exclude={"address": {"id"}})
def read_job(
    *,
    db: Session = Depends(get_db),
    id: int
) -> Any:
    job = job_crud.get(db, id=id)
    if not job:
        raise HTTPException(status_code=404, detail="job not found")
    return job

@router.get("/", response_model=List[schemas.Job], response_model_exclude={"address": {"id"}})
def read_all_jobs(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10000000
) -> Any:
    jobs = job_crud.get_multi(db=db, skip=skip, limit=limit)
    return jobs

@router.post("/", response_model=schemas.Job, response_model_exclude={"address": {"id"}})
def create_job(
    *,
    db: Session = Depends(get_db),
    job_info: schemas.JobCreate
) -> Any:
    job = job_crud.create(db=db, job_info=job_info)
    return job
