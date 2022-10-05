from pydantic import BaseModel

class AssessmentBase(BaseModel):
    uuid: str
    
class AssessmentCreate(BaseModel):
    pass

class AssessmentSubmit(BaseModel):
    uuid: str 
    first_name: str 
    last_name: str 
    email: str 
    phone_number: str

class AssessmentUpdate(AssessmentBase):
    uuid: str | None = None
    owner_id: int | None = None

class AssessmentWithOnlyUuid(AssessmentBase):
    class Config:
        orm_mode = True
