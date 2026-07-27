try:
    name = input("Enter your name: ")

    if name == "":
        raise ValueError("Name cannot be empty.")

    print("Hello", name)

except ValueError as e:
    print("Error:", e)

finally:
    print("Bye Bye!")
