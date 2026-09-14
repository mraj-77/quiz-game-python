questions = [
    {
        "question": "Capital of India kya hai?",
        "answer": "delhi"
    },
    {
        "question": "Capital of Bihar kya hai?",
        "answer": "patna"
    },
    {
        "question": "Prime minister of India kon hai?",
        "answer": "nm"
    },
    {
        "question": "Capital of UP kya hai?",
        "answer": "lakhnau"
    },
]

score = 0

for i in questions:
    print(i["question"]) 
    user_answer = input("Your answer: ")
    
    if user_answer.strip().lower() == i["answer"].lower():
        print("Correct! ✅")
        score = score + 1
    else:
        print(f"Wrong! Correct answer was: {i['answer']}")

print(f"\nYour final score: {score}/{len(questions)}")