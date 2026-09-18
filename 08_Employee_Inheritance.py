class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def show_role(self):
        print("Role: Manager")


manager = Manager("Ananya", 50000)
manager.show_employee()
manager.show_role()
