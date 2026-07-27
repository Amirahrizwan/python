def factorial(n):
    answer = 1

    for i in range(1, n + 1):
        answer = answer * i

    return answer

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not possible for a negative number.")
else:
    print("Factorial:", factorial(number))
