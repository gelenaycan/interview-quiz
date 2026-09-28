import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, tlsCAFile=certifi.where())

try:
    client.admin.command("ping")
    print("Connected successfully")
except Exception as e:
    print("Connection failed:", e)
finally:
    client.close()