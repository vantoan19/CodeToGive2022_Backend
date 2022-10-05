from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from ..db.database import Base


class Job2Label(Base):
    __tablename__ = "job2label"
    job_id = Column(Integer, ForeignKey("jobs.id"), primary_key=True)
    label_id = Column(Integer, ForeignKey("labels.id"), primary_key=True)
    lower_importance_bound = Column(Integer, default=1)
    upper_importance_bound = Column(Integer, default=5)
    
    label_db = relationship("Label")
    label = association_proxy(target_collection="label_db", attr="label")
    

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String)
    description = Column(String)
    company_name = Column(String)
    company_about = Column(String)
    image = Column(String)
    
    address = relationship("Address", uselist=False)
    labels = relationship("Job2Label")
    