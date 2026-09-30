import json
import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())

db = client["interview_quiz"]
collection = db["topics"]      #select database and collection like dictionary keys, if dont exist mongodb creates them auomaticly on the first insert

with open("questions.json", "r", encoding="utf-8") as file:
    data = json.load(file)

collection.delete_many({})#deletes everything in the collection first, without it running script again would create dublicates
result = collection.insert_one(data) #inserts one document and mongodb gives each document a unique Id
print("Inserted with id:", result.inserted_id) 

client.close()