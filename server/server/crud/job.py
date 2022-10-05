import logging
from typing import Any

from fastapi import HTTPException
from server.core.models import Address, Job, Job2Label
from server.core.schemas.job import JobCreate, JobUpdate
from server.crud.base import CRUDBase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .label import label_crud

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDJob(CRUDBase[Job, JobCreate, JobUpdate]):
    
    def create(self, db: Session, *, job_info: JobCreate) -> Job:
        logging.info(f"CRUDJob: Start creating job with job_info\={job_info}")
        job = Job(
            title=job_info.title,
            description=job_info.description,
            company_name=job_info.company_name,
            company_about=job_info.company_about,
            image=job_info.image
        )
        try:
            db.add(job)
            db.flush()
        except SQLAlchemyError:
            logging.error(f"CRUDUser: End creating user with job_info\={job_info}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"CRUDUser: Error at adding in the database")
        if job_info.address:
            job_address = Address(
                job_id=job.id,
                street_line_1=job_info.address.street_line_1,
                street_line_2=job_info.address.street_line_2,
                district=job_info.address.district,
                city=job_info.address.city,
                region=job_info.address.region,
                country=job_info.address.country
            )
            try:
                db.add(job_address)
                db.flush()
            except SQLAlchemyError:
                logging.error(f"CRUDUser: End creating user with job_info\={job_info}: Error", exc_info=True)
                raise HTTPException(status_code=500, detail=f"CRUDUser: Error at adding in the database")
        for label in job_info.labels:
            label_db = label_crud.get_by_label(db=db, label=label.label)
            if not label_db:
                raise HTTPException(status_code=404, detail=f"Label {label.label} does not exist")
            job2label = Job2Label(
                job_id=job.id,
                label_id=label_db.id,
                lower_importance_bound=label.lower_importance_bound,
                upper_importance_bound=label.upper_importance_bound
            )
            try:
                db.add(job2label)
            except SQLAlchemyError:
                logging.error(f"CRUDUser: End creating user with job_info\={job_info}: Error", exc_info=True)
                raise HTTPException(status_code=500, detail=f"CRUDUser: Error at adding in the database")   
        try:
            db.commit()
            db.refresh(job)
            logging.info(f"CRUDUser: End creating user with job_info\={job_info}: Successful")
            return job
        except SQLAlchemyError:
            logging.error(f"CRUDUser: End creating user with job_info\={job_info}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"CRUDUser: Error at committing in the database")

job_crud = CRUDJob(Job)
