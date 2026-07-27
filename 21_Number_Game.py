import math

def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("LCM cannot be found for zero.")
else:
    print("LCM:", find_lcm(a, b))
