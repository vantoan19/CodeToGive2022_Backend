from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from ..db.database import Base


class Answer2Label(Base):
    __tablename__ = "answer2label"
    
    answer_id = Column(Integer, ForeignKey("answers.id"), primary_key=True)
    label_id = Column(Integer, ForeignKey("labels.id"), primary_key=True)
    score = Column(Integer, nullable=False, default=0)
    
    label_obj = relationship("Label")
    label = association_proxy(target_collection="label_obj", attr="label")
    description = association_proxy(target_collection="label_obj", attr="description")
    type = association_proxy(target_collection="label_obj", attr="type")

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), index=True)
    
    labels = relationship("Answer2Label")
    