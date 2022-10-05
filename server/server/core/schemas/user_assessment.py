from .assessment import AssessmentBase
from .user import User
from .test import Test

    
class Assessment(AssessmentBase):
    owner_id: int | None = None
    tests: list[Test]
    owner: User | None = None
    
    class Config:
        orm_mode = True
        
class UserWithAssessment(User):
    assessments: list[Assessment]