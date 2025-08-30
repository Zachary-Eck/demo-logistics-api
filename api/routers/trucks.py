from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Truck
from api.schemas import TruckCreate

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_truck(truck: TruckCreate, db: Session = Depends(get_db)):
    new_truck = Truck(
        driver_name=truck.driver_name,
        capacity=truck.capacity
    )
    db.add(new_truck)
    db.commit()
    db.refresh(new_truck)
    return new_truck

@router.get("/")
def list_trucks(db: Session = Depends(get_db)):
    trucks = db.query(Truck).all()
    return {"trucks": trucks}