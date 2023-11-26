import csv
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    salary: int

    def __repr__(self):
        return f"Employee: name={self.name}, salary={self.salary}"


employees = []
with open("employees.csv") as file:
    employees_file = csv.reader(file)
    next(employees_file)  # přeskočí jeden řádek (hlavičku) v souboru
    for employee in employees_file:
        print(employee)
        employees.append(Employee(employee[0], int(employee[1])))


print(employees)

with open("employees_bak.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['employee', 'salary'])
    for employee in employees:
        writer.writerow([employee.name, employee.salary])