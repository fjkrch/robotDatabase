from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return {"message": "Factory API is running"}

@app.get("/factories")
def read_factories(db: Session = Depends(get_db)):
    return crud.get_factories(db)

@app.get("/machines")
def read_machines(db: Session = Depends(get_db)):
    return crud.get_machines(db)

@app.get("/orders")
def read_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.get("/order-details")
def read_order_details(db: Session = Depends(get_db)):
    return crud.get_order_details(db)

@app.get("/factories/{factory_id}/machines")
def get_machines_by_factory_id(factory_id: str, db: Session = Depends(get_db)):
    return crud.get_machines_by_factory_id(db, factory_id)


@app.get("/machines/{machine_id}/orders")
def get_order_by_machine_id(machine_id: str, db: Session = Depends(get_db)):
    return crud.get_order_by_machine_id(db, machine_id)



@app.get("/orders/{orders_id}/order-details")
def get_order_details_by_order_id(order_id: str, db: Session = Depends(get_db)):
    return crud.get_order_details_by_order_id(db, order_id)

