from pydantic import BaseModel, Field
from server.core.schemas.label import LabelWithScore


class AnswerBase(BaseModel):
    description: str | None = None

class AnswerCreateWithoutQuestionId(AnswerBase):
    labels: list[LabelWithScore]

class AnswerCreate(AnswerBase):
    description: str
    labels: list[LabelWithScore] = []
    question_id: int
    
class AnswerUpdate(AnswerBase):
    labels: list[LabelWithScore] | None = None

class Answer(AnswerBase):
    id: int = Field(alias='answer_id')
    description: str
    question_id: int
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
