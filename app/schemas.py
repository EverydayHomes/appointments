from typing import List, Optional
from pydantic import BaseModel

class AppointmentBase(BaseModel):
    patient_name: str
    appointment_date: str
    appointment_time: str


class AppointmentCreate(AppointmentBase):
    pass



class Appointment(AppointmentBase):
    id: int
    doctor_id: int

    class Config:
        orm_mode = True



class DoctorBase(BaseModel):
    name: str
    specialty: str



class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    appointments: List[Appointment] = []

    class Config:
        orm_mode = True
