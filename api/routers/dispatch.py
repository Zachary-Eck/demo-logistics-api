from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Truck, Job

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/dispatch")
def assign_truck(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    truck = db.query(Truck).filter(Truck.status=="available").first()
    if not truck:
        raise HTTPException(status_code=400, detail="No available trucks")
    job.assigned_truck_id = truck.id
    setattr(truck, "status", "assigned")
    db.commit()
    return {"job_id": job.id, "truck_id": truck.id}