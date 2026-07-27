numbers = [10, 20, 30, 40, 50]

number = int(input("Enter a number: "))

for i in numbers:
    if i == number:
        print("Number is present")
        break
else:
    print("Number is not present")
