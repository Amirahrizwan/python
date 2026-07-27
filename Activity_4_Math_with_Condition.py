import math

number = float(input("Enter a positive number: "))

if number >= 0:
    print("Square root:", math.sqrt(number))
    print("Power of 2:", math.pow(number, 2))
    print("Floor:", math.floor(number))
    print("Ceiling:", math.ceil(number))
else:
    print("Please enter a positive number.")
