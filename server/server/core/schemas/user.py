from pydantic import BaseModel
from server.core.models.user import AccountStatus, AccountType
from server.core.schemas.assessment import AssessmentBase


class UserBase(BaseModel):
    email: str | None
    phone_number: str | None = None
    account_type: AccountType | None = None
    account_status: AccountStatus | None = None
    first_name: str | None = None
    last_name: str | None = None
    
class UserCreate(UserBase):
    email: str 
    account_type: AccountType = AccountType.USER
    account_status: AccountStatus = AccountStatus.NOT_REGISTERED

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class UserWithAssessment(User):
    assessments: AssessmentBase
