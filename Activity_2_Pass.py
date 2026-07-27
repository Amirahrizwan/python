numbers = [10, 20, 30, 40, 50]
search_number = int(input("Enter a number to search: "))

for number in numbers:
    if number == search_number:
        print("Present Number:", number)
        break
else:
    print("Number is not present.")
