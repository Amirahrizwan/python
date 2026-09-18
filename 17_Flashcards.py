flashcards = {
    "Python": "A programming language",
    "Variable": "A name used to store a value",
    "Loop": "Used to repeat a block of code",
    "Function": "A reusable block of code"
}

print("Flashcards")
print("----------")

for question, answer in flashcards.items():
    print("\nQuestion:", question)
    input("Press Enter to see the answer...")
    print("Answer:", answer)
