from fastapi import APIRouter
from database import cars_collection
from models import Car

router=APIRouter()
@router.post("/cars")
def add_car(car: Car):
    cars_collection.insert_one(car.dict())
    return{"msg":"car added successfully!"}
@router.get("/cars")
def get_cars():
    cars= list(cars_collection.find({}, {"_id":0}))
    return{"cars":cars}