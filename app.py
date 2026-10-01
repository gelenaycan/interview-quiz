import os
import certifi
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
collection = client["interview_quiz"]["topics"]

app = Flask(__name__)
CORS(app)

@app.route("/questions")
def get_questions():
    data = collection.find_one({"topic": "Python Basics"}, {"_id": 0})
    return data

app.run(debug=True, port=5001)