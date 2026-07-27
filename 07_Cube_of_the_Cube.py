def get_tip(bill, percent):
    return bill * percent / 100

bill = float(input("Enter the bill amount: "))
percent = float(input("Enter tip percentage: "))

tip = get_tip(bill, percent)

print("Tip:", tip)
print("Total bill:", bill + tip)
