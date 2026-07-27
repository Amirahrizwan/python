try:
    name = input("Enter your name: ")
    if name.strip() == "":
        raise ValueError("Name cannot be empty.")
    print("Hello,", name)
except ValueError as error:
    print("Error:", error)
finally:
    print("Bye Bye!")
