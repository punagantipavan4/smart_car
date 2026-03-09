from pymongo import MongoClient

client=MongoClient()
db=client["smartcar_db"]
cars_collection=db