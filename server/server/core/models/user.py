import enum

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class AccountType(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class AccountStatus(enum.Enum):
    NOT_REGISTERED = "NOT_REGISTERED"
    REGISTERED = "REGISTERED"
    DELETED = "DELETED"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    account_type = Column(Enum(AccountType), default=AccountType.USER)
    account_status = Column(Enum(AccountStatus), default=AccountStatus.NOT_REGISTERED)
    first_name = Column(String)
    last_name = Column(String)
    profile_img = Column(String)
    
    assessments = relationship("Assessment")
    address = relationship("Address", uselist=False)
    