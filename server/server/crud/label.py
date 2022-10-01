import logging
from typing import Any

from fastapi import HTTPException
from server.core.models.label import Label
from server.core.schemas.label import LabelCreate, LabelUpdate
from server.crud.base import CRUDBase
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

class CRUDLabel(CRUDBase[Label, LabelCreate, LabelUpdate]):
    
    def get_by_label(self, db: Session, label: str) -> Label | None:
        logging.info(f"{type(self).__name__}: Start get with label\={label}")
        try:
            label = db.query(self.model).filter(self.model.label == label).first()
            
            logging.info(f"{type(self).__name__}: End get with label\={label}: Successful")
            return label
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End get with label\={label}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")

label_crud = CRUDLabel(Label)
