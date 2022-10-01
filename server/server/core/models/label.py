import enum

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship

from ..db.database import Base


class LabelType(enum.Enum):
    REQUIRED_LABEL = "REQUIRED_LABEL"
    NON_REQUIRED_LABEL = "NON_REQUIRED_LABEL"

class Label(Base):
    __tablename__ = "labels"
    
    id = Column(Integer, primary_key=True)
    type = Column(ENUM(LabelType), nullable=False)
    label = Column(String, unique=True, nullable=False)
    description = Column(String)
    