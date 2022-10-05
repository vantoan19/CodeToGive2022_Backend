from collections import defaultdict

from server.core.models import TestType
from server.crud import assessment_crud, job_crud, question_crud, test_crud
from sqlalchemy.orm import Session

types_of_test = [TestType.ENGLISH_TEST, TestType.MOTIVATION_TEST, TestType.SOCIAL_SITUATION_TEST, TestType.VISIO_PERCEPTUAL_TEST]

def get_suggestion_jobs_for_assessment(db: Session, uuid: str):
    all_jobs = job_crud.get_multi(db=db)
    label_scores = defaultdict(0)
    for test_type in types_of_test:
        test = test_crud.get_test_of_an_assessment(db=db, test_type=test_type, uuid=uuid)
    
