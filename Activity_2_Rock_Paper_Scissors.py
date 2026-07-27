import math

number1 = float(input("Enter first decimal number: "))
number2 = float(input("Enter second decimal number: "))

if math.isclose(number1, number2):
    print("The numbers are close.")
else:
    print("The numbers are not close.")
