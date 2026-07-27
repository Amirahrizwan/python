def check_age(age):
    if age < 0:
        raise Exception("Age cannot be negative.")
    print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except Exception as error:
    print("Exception:", error)
