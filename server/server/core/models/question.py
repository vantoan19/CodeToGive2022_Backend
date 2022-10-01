import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class QuestionType(enum.Enum):
    ABILITY_QUESTION = "ABILITY_QUESTION"
    MOTIVATION_QUESTION = "MOTIVATION_QUESTION"
    ENGLISH_QUESTION = "ENGLISH_QUESTION"
    VISIO_PERCEPTUAL_QUESTION = "VISIO_PERCEPTUAL_QUESTION"
    SOCIAL_SITUATION_QUESTION = "SOCIAL_SITUATION_QUESTION"

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum(QuestionType), nullable=False)
    description = Column(String, nullable=False)
    
    answers = relationship("Answer")
    