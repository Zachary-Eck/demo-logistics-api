from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

class TruckCreate(BaseModel):
    driver_name: str
    capacity: int
    
class JobCreate(BaseModel):
    load_type: str
    destination: str
    scheduled_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))