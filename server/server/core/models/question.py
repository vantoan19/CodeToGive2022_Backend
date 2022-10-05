import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from ..db.database import Base


class QuestionType(enum.Enum):
    MOTIVATION_QUESTION = "MOTIVATION_QUESTION"
    ENGLISH_QUESTION = "ENGLISH_QUESTION"
    VISIO_PERCEPTUAL_QUESTION = "VISIO_PERCEPTUAL_QUESTION"
    SOCIAL_SITUATION_QUESTION = "SOCIAL_SITUATION_QUESTION"

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum(QuestionType), nullable=False)
    description = Column(String, nullable=False)
    img_url = Column(String)
    img_alt = Column(String)
    
    answers = relationship("Answer", cascade="all")
    
    @hybrid_property
    def tags(self):
        tags_set = set()
        for answer in self.answers:
            for label in answer.labels:
                tags_set.add(label.label)
        return list(tags_set)
    