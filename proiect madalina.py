
import pandas as pd
class Employee:
    def __init__(self, emp_id, name, position, salary, hire_date, department):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date
        self.department = department

    def __repr__(self):
         return (f"employee:{self.emp_id}, name:{self.name}, position:{self.position}, salary:{self.salary}, hire date:{self.hire_date}, department: {self.department}")

class Database:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
         self.employees.append(employee)
    def calculate_employee_salary(self, gross_salary):
        tax_rate = 0.25
        net_salary = gross_salary * (1 - tax_rate)
        return net_salary


CompanyDatabase = Database()

employees_data = [
    (1, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
    (2, "Elena", "customer analist", 5000,  "2015-08-15", "Support"),
    (3, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
    (4, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
    (5, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
    (6, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
    (7, "Elena", "customer analist", 4500,  "2015-08-15", "Support"),
 ]

for emp in employees_data:
    CompanyDatabase.add_employee(emp)
for emp in CompanyDatabase.employees:
     gross_salary = emp[3]
     net_salary = CompanyDatabase.calculate_employee_salary(gross_salary)
     print(f"Salariu brut: {gross_salary}")
     print(f"Salariu net: {net_salary}")