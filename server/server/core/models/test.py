import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship 

from ..db.database import Base

class TestType(enum.Enum):
    ABILITY_TEST = 1
    MOTIVATION_TEST = 2
    ENGLISH_TEST = 3
    VISIO_PERCEPTUAL_TEST = 4
    SOCIAL_SITUATION_TEST = 5

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"), index=True)
    type = Column(Enum(TestType), nullable=False)
    