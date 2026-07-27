import math

number = float(input("Enter a positive number: "))

if number >= 0:
    print("Square root:", math.sqrt(number))
    print("Square:", math.pow(number, 2))
    print("Floor value:", math.floor(number))
    print("Ceiling value:", math.ceil(number))
else:
    print("Please enter a positive number.")
