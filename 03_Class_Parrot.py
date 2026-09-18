class Parrot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        print(self.name, "says: Hello!")

    def show_details(self):
        print("Name:", self.name)
        print("Color:", self.color)


parrot = Parrot("Mithu", "Green")
parrot.show_details()
parrot.speak()
