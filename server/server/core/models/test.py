import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from ..db.database import Base


def get_completed(questions) -> bool:
    for question in questions:
        if not question.answered_id:
            return False
    return True

def get_progress(questions) -> int:
    number_of_answered_question = 0
    for question in questions:
        number_of_answered_question += 1 if question.answered_id else 0
    return (100 if len(questions) == 0 
            else number_of_answered_question * 100 // len(questions))

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
    img_url = association_proxy(target_collection="question", attr="img_url")
    img_alt = association_proxy(target_collection="question", attr="img_alt")

class TestType(enum.Enum):
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
    description = Column(String)
    
    @hybrid_property
    def url(self):
        return f"/assessments/{self.assessment_uuid}/tests?test_type={self.type.value}"
    
    questions = relationship("Test2Question")
    
    @hybrid_property
    def completed(self):
        return get_completed(self.questions)
    
    @hybrid_property
    def progress(self):
        return get_progress(self.questions)
    