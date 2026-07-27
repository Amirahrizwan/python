total_amount = float(input("Enter the total amount: "))
paid_amount = float(input("Enter the amount paid: "))

if paid_amount >= total_amount:
    print("No amount is due.")
    print("Change to return:", paid_amount - total_amount)
else:
    due_amount = total_amount - paid_amount
    print("Due amount:", due_amount)
