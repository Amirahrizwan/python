def weather_condition(temp):
    if temp > 30:
        print("It is hot today.")
    elif temp < 15:
        print("It is cold today.")
    else:
        print("The weather is pleasant.")

temp = float(input("Enter the temperature: "))
weather_condition(temp)
