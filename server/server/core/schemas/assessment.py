from pydantic import BaseModel
from server.core.schemas.test import Test


class AssessmentBase(BaseModel):
    uuid: str
    
class AssessmentCreate(AssessmentBase):
    pass

# No support in assessment update
# Reason: assessment are automatically generated
class AssessmentUpdate(AssessmentBase):
    pass

class Assessment(AssessmentBase):
    owner_id: int | None = None
    tests: list[Test]
    
    class Config:
        orm_mode = True
