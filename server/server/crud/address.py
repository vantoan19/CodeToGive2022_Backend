import logging
from typing import Any

from fastapi import HTTPException
from server.core.models.address import Address
from server.core.schemas.address import AddressCreate, AddressUpdate
from server.crud.base import CRUDBase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDAddress(CRUDBase[Address, AddressCreate, AddressUpdate]):
    pass

address_crud = CRUDAddress(Address)
