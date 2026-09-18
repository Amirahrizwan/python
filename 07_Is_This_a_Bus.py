class Vehicle:
    pass


class Bus(Vehicle):
    pass


vehicle = Bus()

if isinstance(vehicle, Bus):
    print("Yes, this is a Bus.")
else:
    print("No, this is not a Bus.")
