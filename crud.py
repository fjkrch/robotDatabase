from sqlalchemy.orm import Session
import models

def get_factories(db: Session):
    return db.query(models.Factory).all()

def get_machines(db: Session):
    return db.query(models.Machine).all()

def get_orders(db: Session):
    return db.query(models.Order).all()

def get_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def get_machines_by_factory_id(db: Session, factory_id: str):
    return db.query(models.Machine).filter(models.Machine.factory_id == factory_id).all()

def get_order_by_machine_id(db: Session, machine_id: str):
    return db.query(models.Order).filter(models.Order.machine_id == machine_id).all()

def get_order_details_by_order_id(db: Session, order_id: str):
    return db.query(models.OrderDetail).filter(models.OrderDetail.order_id== order_id).all()
