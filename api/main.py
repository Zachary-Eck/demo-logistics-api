from fastapi import FastAPI
from api.models import Base
from api.database import engine
from api.routers import jobs, trucks, dispatch  # Import the routers

app = FastAPI(title="Logistics Dispatch API")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Logistics Dispatch API"}

app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(trucks.router, prefix="/trucks", tags=["trucks"])
app.include_router(dispatch.router, prefix="/dispatch", tags=["dispatch"])