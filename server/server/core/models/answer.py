from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship 

from ..db.database import Base


class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    