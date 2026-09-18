class Bird:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Bird name:", self.name)


class Penguin(Bird):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        super().show()
        print("Age:", self.age)
        print("Penguin can swim.")


penguin = Penguin("Pingu", 3)
penguin.show()
