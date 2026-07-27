def employee_details(name, employee_id, salary):
    print("\nEmployee Details")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Salary:", salary)

name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

employee_details(name, employee_id, salary)
