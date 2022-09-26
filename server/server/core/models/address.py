from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship 

from ..db.database import Base


class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True)
    street_line_1 = Column(String)
    street_line_2 = Column(String)
    district = Column(String)
    city = Column(String)
    region = Column(String)
    country = Column(String)
    