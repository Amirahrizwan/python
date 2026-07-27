try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Value Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Zero Division Error: Cannot divide by zero.")
