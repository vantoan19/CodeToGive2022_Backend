import logging
from typing import Any, Dict

from fastapi import HTTPException
from server.core.models import Assessment, TestType
from server.core.schemas import AssessmentCreate, AssessmentUpdate, TestCreate
from server.crud.crud_exception import NotImplementedException
from server.lib.uuid_utils import generate_unique_uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .base import CRUDBase
from .test import test_crud

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

types_of_test = [TestType.ABILITY_TEST, TestType.ENGLISH_TEST, TestType.MOTIVATION_TEST, TestType.SOCIAL_SITUATION_TEST, TestType.VISIO_PERCEPTUAL_TEST]

default_desc = "Tell more about your interests so you can find the most suitable job."

class CRUDAssessment(CRUDBase[Assessment, AssessmentCreate, AssessmentUpdate]):
    
    def get(self, db: Session, id: Any) -> Assessment | None:
        raise NotImplementedException(crud_component="Assessment", crud_operation="Get")
    
    def get_by_uuid(self, db: Session, uuid: str) -> Assessment | None:
        logging.info(f"CRUDAssessment: Start query with uuid\={uuid}")
        try:
            assessment = db.query(self.model).filter(self.model.uuid == uuid).first()
            
            logging.info(f"CRUDAssessment: End query with uuid\={uuid}: Successful")
            return assessment
        except SQLAlchemyError:
            logging.error(f"CRUDAssessment: End query with uuid\={uuid}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")
    
    def update(self, db: Session, *, db_obj: Assessment, obj_in: AssessmentUpdate | Dict[str, Any]) -> Assessment:
        raise NotImplementedException(crud_component="Assessment", crud_operation="Update")
    
    def generate_assessment(self, db: Session) -> Assessment:
        logging.info(f"CRUDAssessment: Start generate assessment")
        
        uuid = generate_unique_uuid()
        assessment = Assessment(uuid=uuid)
        try:
            db.add(assessment)
            db.flush()
        except:
            logging.error(f"CRUDAssessment: End generate assessment: Error", exc_info=True)
            db.rollback()
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at adding the database")
        
        for type in types_of_test:
            try:
                test_schema = TestCreate(type=type, assessment_uuid=assessment.uuid, description=default_desc)
                test_crud.generate_test(db=db, test_info=test_schema)
            except Exception as e:
                logging.error(f"CRUDAssessment: End generate assessment: Error", exc_info=True)
                raise e
            
        db.refresh(assessment)
        logging.info(f"CRUDAssessment: End generate assessment: Successful, uuid\={uuid}")
        return assessment
        
assessment_crud = CRUDAssessment(Assessment)
