from pydantic import BaseModel, Field
from server.core.models.user import AccountStatus, AccountType

from .address import AddressBase, AddressUserId


class UserBase(BaseModel):
    email: str | None
    phone_number: str | None = None
    account_type: AccountType | None = None
    account_status: AccountStatus | None = None
    first_name: str | None = None
    last_name: str | None = None
    profile_img: str | None = None
    
class UserCreate(UserBase):
    email: str 
    account_type: AccountType = AccountType.USER
    account_status: AccountStatus = AccountStatus.NOT_REGISTERED
    address: AddressBase | None = None

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int = Field(alias="user_id")
    address: AddressUserId | None = None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

