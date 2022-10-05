import enum

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship

from ..db.database import Base


class LabelType(enum.Enum):
    REQUIRED_LABEL = "REQUIRED_LABEL"
    NON_REQUIRED_LABEL = "NON_REQUIRED_LABEL"
    
class LabelCategory(enum.Enum):
    MOTIVATION_LABEL = "MOTIVATION_LABEL"
    ENGLISH_LABEL = "ENGLISH_LABEL"
    VISIO_PERCEPTUAL_LABEL = "VISIO_PERCEPTUAL_LABEL"
    SOCIAL_SITUATION_LABEL = "SOCIAL_SITUATION_LABEL"

class Label(Base):
    __tablename__ = "labels"
    
    id = Column(Integer, primary_key=True)
    type = Column(ENUM(LabelType), nullable=False)
    category = Column(ENUM(LabelCategory), nullable=False)
    label = Column(String, unique=True, nullable=False)
    description = Column(String)
