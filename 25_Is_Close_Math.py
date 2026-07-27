import math

number = float(input("Enter a number: "))

if number > 0:
    print("Square root:", math.sqrt(number))

elif number == 0:
    print("The number is zero.")

else:
    print("Square root cannot be found for a negative number.")
