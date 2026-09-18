class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Class:", self.grade)


student = Student("Aarav", 12, 7)
student.display()
