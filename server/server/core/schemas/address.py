from pydantic import BaseModel


class AddressBase(BaseModel):
    street_line_1: str | None = None
    street_line_2: str | None = None
    district: str | None = None
    city: str | None = None
    region: str | None = None
    country: str | None = None
    
class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    class Config:
        orm_mode = True

class AddressUserId(Address):
    user_id: int 
    
    class Config:
        orm_mode = True

class AddressJobId(Address):
    job_id: int
    
    class Config:
        orm_mode = True

