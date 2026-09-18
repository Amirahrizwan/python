class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price: ₹", self.price)


computer = Computer("Dell", 55000)
computer.display()
