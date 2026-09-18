countries = {
    "India": {
        "capital": "New Delhi",
        "continent": "Asia",
        "language": "Hindi",
        "currency": "Indian Rupee"
    },
    "Japan": {
        "capital": "Tokyo",
        "continent": "Asia",
        "language": "Japanese",
        "currency": "Yen"
    },
    "France": {
        "capital": "Paris",
        "continent": "Europe",
        "language": "French",
        "currency": "Euro"
    }
}

country = input("Enter a country: ")

if country in countries:
    print("\nCountry:", country)
    for key, value in countries[country].items():
        print(key.title() + ":", value)
else:
    print("Country not found.")
