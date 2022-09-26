import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship 

from ..db.database import Base

class QuestionType(enum.Enum):
    ABILITY_QUESTION = 1
    MOTIVATION_QUESTION = 2
    ENGLISH_QUESTION = 3
    VISIO_PERCEPTUAL_QUESTION = 4
    SOCIAL_SITUATION_QUESTION = 5

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum(QuestionType), nullable=False)
    description = Column(String, nullable=False)
    
    