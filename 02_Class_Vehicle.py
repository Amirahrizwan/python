class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")


car = Vehicle("Toyota", 120)
car.show_details()
