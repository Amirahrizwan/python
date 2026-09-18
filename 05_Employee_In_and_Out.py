class Employee:
    def __init__(self, name):
        self.name = name
        self.inside = False

    def check_in(self):
        self.inside = True
        print(self.name, "has entered the office.")

    def check_out(self):
        self.inside = False
        print(self.name, "has left the office.")


employee = Employee("Rahul")

employee.check_in()
employee.check_out()
