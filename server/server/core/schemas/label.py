from unicodedata import category
from pydantic import BaseModel, Field
from server.core.models import LabelType, LabelCategory


class LabelBase(BaseModel):
    label: str | None = None


class LabelWithScore(LabelBase):
    label: str
    score: int
    max_score: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class LabelWithTotalScore(LabelBase):
    total_score: int
    total_max_score: int


class LabelWithImportance(LabelBase):
    label: str
    lower_importance_bound: int = 1
    upper_importance_bound: int = 5

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class LabelCreate(LabelBase):
    type: LabelType = LabelType.NON_REQUIRED_LABEL
    category: LabelCategory
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
    category: LabelCategory
    label: str
    description: str | None = None

    class Config:
        orm_mode = True
