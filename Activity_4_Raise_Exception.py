try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Value Error: Please enter a valid integer.")
