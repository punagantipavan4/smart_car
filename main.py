""" from fastapi import FastAPI
from routers.cars import router

app=FastAPI()
app.include_router(router)

@app.get("/")
def newone():
  return{"msg":"smart car service running!"}
 """
from fastapi import FastAPI
from routes.cars import router as cars_router
from routes.auth import router as auth_router
from routes.bookings import router as bookings_router

app=FastAPI()
app.include_router(cars_router)
app.include_router(auth_router)
app.include_router(bookings_router)
@app.get("/")
def newone():
  return{"msg":"smart car service running!"}
