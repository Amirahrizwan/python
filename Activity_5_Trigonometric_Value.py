age = int(input("Enter your current age: "))

print("Your age for the next 10 years:")

for year in range(1, 11):
    print("After", year, "year(s):", age + year)
