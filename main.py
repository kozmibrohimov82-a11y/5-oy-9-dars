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

@app.post("/doctors/",response_model=DoctorResponse)
async def create_doctor_endpoint(doctor:DoctorCreate,db:AsyncSession=Depends(get_db)):
    return await crud.create_doctor(doctor,db)

@app.get("/doctors/",response_model=list[DoctorResponse])
async def get_all(db:AsyncSession=Depends(get_db)):
    return await crud.read_doctors(db)

@app.get("/doctors/{doctor_id}/",response_model=DoctorResponse)
async def get_one(doctor_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.read_doctor(doctor_id,db)

@app.put("/doctors/{doctor_id}/",response_model=DoctorResponse)
async def update(doctor_id:int,doctor:DoctorCreate,db:AsyncSession=Depends(get_db)):
    return await crud.update_doctor(doctor_id,doctor,db)

@app.delete("/doctors/{doctor_id}/",response_model=dict)
async def delete(doctor_id:int,db:AsyncSession=Depends(get_db)):
    return await crud.delete_doctor(doctor_id,db)


if __name__ == '__main__':
    uvicorn.run(app)