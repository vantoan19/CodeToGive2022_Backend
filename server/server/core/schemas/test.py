from pydantic import BaseModel, Field
from server.core.models import TestType
from server.core.schemas.question import QuestionWithAnsweredId


class TestBase(BaseModel):
    type: TestType 
    title: str | None
    description: str

class TestCreate(TestBase):
    assessment_uuid: str
    
# No support in test update
# Reason: Tests are automatically generated
class TestUpdate(TestBase):
    pass    

class Test(TestBase):
    id: int = Field(alias="test_id")
    assessment_uuid: str 
    questions: list[QuestionWithAnsweredId]
    url: str
    completed: bool
    progress: int
    
    class Config: 
        orm_mode = True
        allow_population_by_field_name = True
