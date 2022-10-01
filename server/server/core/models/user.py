import enum

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class AccountType(enum.Enum):
    ADMIN = 1
    USER = 2

class AccountStatus(enum.Enum):
    NOT_REGISTERED = 1
    REGISTERED = 2

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    account_type = Column(Enum(AccountType), default=AccountType.USER)
    account_status = Column(Enum(AccountStatus), default=AccountStatus.NOT_REGISTERED)
    first_name = Column(String)
    last_name = Column(String)
    
    assessments = relationship("Assessment", back_populates="owner")
    address = relationship("Address")
    