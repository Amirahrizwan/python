questions = {
    "What fruit is yellow and monkeys like to eat? ": "banana",
    "What fruit is usually red or green and grows on trees? ": "apple",
    "What fruit is known for having a crown on top? ": "pineapple",
    "What small fruit is commonly purple or green and grows in bunches? ": "grape"
}

score = 0

print("Fruit Quiz")
print("----------")

for question, answer in questions.items():
    user_answer = input(question).strip().lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", answer)

print("\nQuiz completed!")
print("Your score:", score, "/", len(questions))
