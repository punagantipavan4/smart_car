from fastapi import APIRouter
from pydantic import BaseModel
from database import bookings_collection
from datetime import datetime
from bson import objectid

router=APIRouter()
class Booking(BaseModel):
  user_email:str
  car_brand:str
  car_model:str
  pickup_date:str
  return_date:str
  pickup_location:str
@router.post("/bookings")
def create_bookings(booking: Booking):
  bookings_collection.insert_one({
  "user_email":booking.user_email,
  "car_brand":booking.car_brand,
  "car_model":booking.car_model,
  "pickup_udate":booking.pickup_date,
  "return_date":booking.return_date,
  "pickup_location":booking.pickup_location,
  "status":"confirmed",
  "created_at":datetime.utcnow().strftime("%y-%m-%d %H:%M:%S")
 }) 
  return{"msg":"booking created successfully"}
@router.get("/bookings")
def get_bookings():
  bookings=list(bookings_collection.find({}, {"_id":0}))
  return{"bookings": bookings}
@router.put("/bookings/{booking_id}")
def update_booking(booking_id:str):
  bookings_collection.update_one(
    {"_id": objectid(booking_id)},
    {"$set":{"status":"cancelled"}}
  )
  return{"msg":"booking updated sucessfuly"}
# delete booking
@router.delete("/bookings/{bookings_id}")
def delete_booking(bookings_id:str):
  bookings_collection.delete_one(
    {"_id": objectid(bookings_id)}
  )
  return{"msg":"booking deleted successfully"}

