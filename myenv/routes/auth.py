from fastapi import APIRouter
from pydantic import BaseModel
from jose import jwt
from datetime import datetime,timedelta
from database import users_collection

router=APIRouter()
# pasword hasing
# jwt settings
secret_key="smartcar123"
Algorithm="HS256"
Expire_MINUTES=30
# user models
class UserRegisters(BaseModel):
  name:str
  email:str
  password:str
class UserLogin(BaseModel):
  email:str
  password:str
#create jwt token function
def create_token(email:str):
  expire=datetime.utcnow()+timedelta(minutes=Expire_MINUTES)
  data={"email":email,"exp":expire}
  token=jwt.encode(data, secret_key, algorithm=Algorithm)
  return token
# regestired api
@router.post("/register")
def register(user : UserRegisters):
  # check if mail already exists{
  existing_user=users_collection.find_one({"email": user.email})
  if existing_user:
    return{"msg":"Email already registered!"}
  # hash password
  users_collection.insert_one({
    "name":user.name,
    "email":user.email,
    "password":user.password
  })
  return{
    "msg":"user registeration successfully",
    "name":user.name,
    "email":user.email
  }
# login api
@router.post("/login")
def login(user:UserLogin):
  db_user=users_collection.find_one({"email":user.email})
  if not db_user:
    return{"msg":"email not found"}
  if user.password!=db_user["password"]:
    return{"msg":"wrong password!"}
  token=create_token(user.email)
  return{
    "msg" : "login successfull",
    "email" : user.email,
    "token": token
  }


