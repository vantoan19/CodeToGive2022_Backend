from pydantic import BaseModel, Field
from server.core.models.question import QuestionType
from server.core.schemas.answer import (Answer, AnswerBase,
                                        AnswerCreateWithoutQuestionId)


class QuestionBase(BaseModel):
    type: QuestionType | None = None
    description: str | None = None
    answers: list[AnswerBase] | None = None


class QuestionCreate(QuestionBase):
    type: QuestionType
    description: str
    answers: list[AnswerCreateWithoutQuestionId]

class MotivationQuestionCreate(BaseModel):
    type: QuestionType = QuestionType.MOTIVATION_QUESTION
    description: str
    labels: list[str]

class QuestionUpdate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int = Field(alias='question_id')
    type: QuestionType
    description: str
    answers: list[Answer]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class QuestionWithAnsweredId(Question):
    answered_id: int | None
