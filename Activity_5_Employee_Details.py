def calculate_tip(bill, tip_percent):
    return bill * tip_percent / 100

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
tip = calculate_tip(bill, tip_percent)

print("Tip amount:", tip)
print("Total amount:", bill + tip)
