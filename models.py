from sqlalchemy import String,ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped,mapped_column,relationship

from database import Base

class Doctor(Base):
    __tablename__ = "doctor"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150))
    phone_number: Mapped[str] = mapped_column(String(14))
    job:Mapped[str]=mapped_column(String(50))
    patient:Mapped["Patient"]=relationship(back_populates="doctor")

class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150))
    sick_kind:Mapped[str]=mapped_column(String(150))
    doctor_id:Mapped[int]=mapped_column(ForeignKey("doctor.id"))

    doctor:Mapped["Doctor"]=relationship(back_populates="patient")
