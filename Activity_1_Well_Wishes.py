def weather_condition(temperature):
    if temperature > 30:
        return "It is hot outside."
    elif temperature < 15:
        return "It is cold outside."
    else:
        return "The weather is pleasant."

temperature = float(input("Enter the temperature: "))
print(weather_condition(temperature))
