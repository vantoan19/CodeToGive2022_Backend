import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from ..db.database import Base


class Test2Question(Base):
    __tablename__ = "test2question"
    
    test_id = Column(Integer, ForeignKey("tests.id"), primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    answered_id = Column(Integer, ForeignKey("answers.id"), nullable=True, default=None)
    
    question = relationship("Question")
    answered = relationship("Answer")
    type = association_proxy(target_collection="question", attr="type")
    description = association_proxy(target_collection="question", attr="description")
    answers = association_proxy(target_collection="question", attr="answers")

class TestType(enum.Enum):
    ABILITY_TEST = "ABILITY_TEST"
    MOTIVATION_TEST = "MOTIVATION_TEST"
    ENGLISH_TEST = "ENGLISH_TEST"
    VISIO_PERCEPTUAL_TEST = "VISIO_PERCEPTUAL_TEST"
    SOCIAL_SITUATION_TEST = "SOCIAL_SITUATION_TEST"

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True)
    assessment_uuid = Column(String, ForeignKey("assessments.uuid"), index=True)
    title = Column(String)
    type = Column(Enum(TestType), nullable=False)
    
    questions = relationship("Test2Question")
    