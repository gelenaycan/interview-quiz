import json
with open("questions.json","r", encoding="utf-8") as file:  #with with we dont need to use close(), automaticly done
    data =json.load(file) 

print(data["topic"])
print(data["lesson"])

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