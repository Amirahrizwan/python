def calculator(a, b, choice):
    if choice == "+":
        return a + b
    elif choice == "-":
        return a - b
    elif choice == "*":
        return a * b
    elif choice == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid choice"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choice = input("Enter +, -, * or /: ")

print("Answer:", calculator(a, b, choice))
