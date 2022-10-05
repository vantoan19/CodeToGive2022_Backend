import logging
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from server.core.db.database import Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.DEBUG ,format='%(process)d-%(levelname)s-%(message)s')

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        logging.info(f"{type(self).__name__}: Start query with id\={id}")
        try:
            obj = db.query(self.model).filter(self.model.id == id).first()
            
            logging.info(f"{type(self).__name__}: End query with id\={id}: Successful")
            return obj
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End query with id\={id}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 1000000
    ) -> List[ModelType]:
        logging.info(f"{type(self).__name__}: Start multiple query")
        try:
            objs = db.query(self.model).offset(skip).limit(limit).all()
            
            logging.info(f"{type(self).__name__}: End multiple query: Successful")
            return objs
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End multiple query: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at querying the database")

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        logging.info(f"{type(self).__name__}: Start creating with schema\={obj_in}")
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            
            logging.info(f"{type(self).__name__}: End creating with schema\={obj_in}: Successful")
            return db_obj
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End creating with schema\={obj_in}: Error", exc_info=True)
            db.rollback()
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at committing in the database")

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | Dict[str, Any]
    ) -> ModelType:
        logging.info(f"{type(self).__name__}: Start updating with schema\={obj_in}")
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        logging.info(obj_data)
        for field in obj_data:
            logging.info(field)
            logging.info(obj_data)
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            
            logging.info(f"{type(self).__name__}: End updating with schema\={obj_in}: Successful")
            return db_obj
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End updating with schema\={obj_in}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at committing in the database")

    def remove(self, db: Session, *, id: int) -> ModelType:
        logging.info(f"{type(self).__name__}: Start removing id\={id}")
        obj = db.query(self.model).get(id)
        if not obj:
            logging.error(f"{type(self).__name__}: End removing id\={id}: Not exist")
            raise HTTPException(status_code=404, detail=f"{type(self).__name__}: Question does not exist")
        try:
            db.delete(obj)
            db.commit()
            
            logging.info(f"{type(self).__name__}: End removing id\={id}: Successful")
            return obj
        except SQLAlchemyError:
            logging.error(f"{type(self).__name__}: End removing id\={id}: Error", exc_info=True)
            raise HTTPException(status_code=500, detail=f"{type(self).__name__}: Error at committing the database")
    