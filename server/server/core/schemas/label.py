from pydantic import BaseModel
from server.core.models import LabelType


class LabelBase(BaseModel):
    label: str | None = None

class LabelWithScore(LabelBase):
    label: str
    score: int
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
    

class LabelCreate(LabelBase):
    type: LabelType = LabelType.NON_REQUIRED_LABEL
    label: str
    description: str | None = None
    
    class Config:
        use_enum_values = True

class LabelUpdate(LabelBase):
    type: LabelType | None = None
    description: str | None = None
    
class Label(LabelBase):
    id: int
    type: LabelType
    label: str
    description: str | None = None
    
    class Config:
        orm_mode = True
