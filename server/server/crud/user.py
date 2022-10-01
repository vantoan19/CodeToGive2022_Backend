from server.core.models.user import User
from server.core.schemas.user import UserCreate, UserUpdate
from server.crud.base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass

user_crud = CRUDUser(User)
