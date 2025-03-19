from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["clothing_store"]
products_collection = db["products"]
