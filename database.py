from pymongo import MongoClient

client=MongoClient()
db=client["smartcar_db"]
cars_collection=db["cars"]
users_collection=db["users"]
bookings_collection=db["bookings"]