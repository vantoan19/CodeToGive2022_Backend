import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship 

from ..db.database import Base

class LabelType(enum.Enum):
    REQUIRED_LABEL = 1
    NON_REQUIRED_LABEL = 2

class Label(Base):
    __tablename__ = "labels"
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum(LabelType))
    label = Column(String, unique=True, nullable=False)
    description = Column(String)
    
    