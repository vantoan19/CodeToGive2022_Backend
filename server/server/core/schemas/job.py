from pydantic import BaseModel, Field
from server.core.models.user import AccountStatus, AccountType
from server.core.schemas.label import LabelWithImportance

from .address import AddressBase, Address


class JobBase(BaseModel):
    title: str | None = None
    description: str | None = None
    company_name: str | None = None
    company_about: str | None = None
    image: str | None = None
    labels: list[LabelWithImportance] | None = None


class JobCreate(JobBase):
    title: str
    description: str
    company_name: str
    labels: list[LabelWithImportance]
    address: AddressBase


class JobUpdate(JobBase):
    pass


class Job(JobBase):
    id: int = Field(alias="job_id")
    address: Address | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class JobWithMatchScore(Job):
    match_score: int
