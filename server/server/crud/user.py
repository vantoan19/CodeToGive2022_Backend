import logging

from fastapi import HTTPException
from server.core.models import Address, User
from server.core.schemas.user import UserCreate, UserUpdate
from server.crud.base import CRUDBase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    
    def create(self, db: Session, *, user_info: UserCreate) -> User:
        logging.info(f"CRUDUser: Start creating user with user_info\={user_info}")
        user = User(
            email=user_info.email,
            phone_number=user_info.phone_number,
            account_type=user_info.account_type,
            account_status=user_info.account_status,
            first_name=user_info.first_name,
            last_name=user_info.last_name,
            profile_img=user_info.profile_img
        )
        try:
            db.add(user)
            db.flush()
        except SQLAlchemyError:
            logging.error(f"CRUDUser: End creating user with user_info\={user_info}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"CRUDUser: Error at adding in the database")
        if user_info.address:
            user_address = Address(
                user_id=user.id,
                street_line_1=user_info.address.street_line_1,
                street_line_2=user_info.address.street_line_2,
                district=user_info.address.district,
                city=user_info.address.city,
                region=user_info.address.region,
                country=user_info.address.country
            )
            db.add(user_address)
        try:
            db.commit()
            db.refresh(user)
            return user
        except SQLAlchemyError:
            logging.error(f"CRUDUser: End creating user with user_info\={user_info}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"CRUDUser: Error at committing in the database")
        
        
        
user_crud = CRUDUser(User)
