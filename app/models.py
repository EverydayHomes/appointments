from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, index=True)
    patient_email = Column(String, index=True)
    scheduled_time = Column(String, index=True)
    canceled = Column(Boolean, default=False)