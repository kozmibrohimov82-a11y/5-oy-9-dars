from fastapi.params import Depends
from fastapi import FastAPI
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession

from database import *
from schemas import *
import crud

app=FastAPI()

async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.post("/doctors/",response_model=DoctorResponse,tags=["Doctors"])
async def create_doctor_endpoint(doctor:DoctorCreate,db:AsyncSession=Depends(get_db)):
    return await crud.create_doctor(doctor,db)

@app.get("/doctors/",response_model=list[DoctorResponse],tags=["Doctors"])
async def get_all(db:AsyncSession=Depends(get_db)):
    return await crud.read_doctors(db)

@app.get("/doctors/{doctor_id}/",response_model=DoctorResponse,tags=["Doctors"])
async def get_one(doctor_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.read_doctor(doctor_id,db)

@app.put("/doctors/{doctor_id}/",response_model=DoctorResponse,tags=["Doctors"])
async def update(doctor_id:int,doctor:DoctorCreate,db:AsyncSession=Depends(get_db)):
    return await crud.update_doctor(doctor_id,doctor,db)

@app.delete("/doctors/{doctor_id}/",response_model=dict,tags=["Doctors"])
async def delete(doctor_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.delete_doctor(doctor_id,db)
##################################################################################

@app.post("/patients/",response_model=PatientResponse,tags=["Patient"])
async def create_patient_endpoint(patient:PatientCreate,db:AsyncSession=Depends(get_db)):
    return await crud.create_patient(patient,db)

@app.get("/patients/",response_model=list[PatientResponse],tags=["Patient"])
async def get_all(db:AsyncSession=Depends(get_db)):
    return await crud.read_patients(db)

@app.get("/patients/{patient_id}/",response_model=PatientResponse,tags=["Patient"])
async def get_one(patient_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.read_patient(patient_id,db)

@app.put("/patients/{patient_id}/",response_model=PatientResponse,tags=["Patient"])
async def update(patient_id:int,patient:PatientCreate,db:AsyncSession=Depends(get_db)):
    return await crud.update_patient(patient_id,patient,db)

@app.delete("/patients/{patient_id}/",response_model=dict,tags=["Patient"])
async def delete(patient_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.delete_patient(patient_id,db)














if __name__ == '__main__':
    uvicorn.run(app)