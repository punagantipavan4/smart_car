from fastapi import FastAPI
from routers.cars import router

app=FastAPI()
app.include_router(router)

@app.get("/")
def newone():
  return{"msg":"smart car service running!"}
