from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from schemas import ShipmentUpdate
from services import update_shipment_service

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.put("/shipments/{shipment_id}")
def update_shipment(shipment_id: int,shipment_update: ShipmentUpdate,db: Session = Depends(get_db)):
    return update_shipment_service(db,shipment_id,shipment_update)