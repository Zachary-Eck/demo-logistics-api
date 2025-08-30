from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Truck(Base):
    __tablename__ = "trucks"
    id = Column(Integer, primary_key=True)
    driver_name = Column(String)
    capacity = Column(Integer)
    status = Column(String, default="available")

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    load_type = Column(String)
    destination = Column(String)
    scheduled_time = Column(DateTime)
    assigned_truck_id = Column(Integer, ForeignKey("trucks.id"), nullable=True)
    truck = relationship("Truck")
