class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound.")


class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof!")


dog = Dog("Bruno")
dog.speak()
