import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
collection = client["interview_quiz"]["topics"]

data = collection.find_one({"topic":"Python Basics"})

print(data["topic"])
print(data["lesson"])
print()

score=0
for question in data["questions"]:
    print(question["question"])
    for i, option in enumerate(question["options"],start=1):
        print(f"{i}: {option}")

    while True:
        choice = input("Your answer (number): ")
        try:
            selected = question["options"][int(choice)-1]
            break #exist the infinite loop, important
        except(ValueError,IndexError):
            print("Please enter a valid number.")

    if selected == question["answer"]:
        print("thats correcttt")
        score +=1
        
    else:
        print(f"wrong... correct answer: {question['answer']}")
 
    print()

total = len(data["questions"])
print(f"Your score: {score}/{total}")
percantage = score / total *100

if percantage >=80:
    level = "GOOOD"
elif percantage >=50:
    level = "intermediate"
else:
    level = "beginner"

print(f"Your level: {level}")