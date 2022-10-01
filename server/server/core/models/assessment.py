from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class Assessment(Base):
    __tablename__ = "assessments"
    
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    uuid = Column(String, primary_key=True, unique=True, index=True)
    
    owner = relationship("User", back_populates="assessments")
    tests = relationship("Test")
    