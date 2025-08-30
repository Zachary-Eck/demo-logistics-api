from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Job
from api.schemas import JobCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(
        load_type=job.load_type,
        destination=job.destination,
        scheduled_time=job.scheduled_time
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return {"jobs": jobs}