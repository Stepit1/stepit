import pandas as pd
class Manager:
    def __init__(self, mgr_id, name, department, salary, hire_date, bonus):
        self.mgr_id = mgr_id
        self.name = name
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
        self.bonus = bonus

    def __repr__(self):
        return f"manager(id): {self.mgr_id}, name: {self.name}, department: {self.department}, salary: {self.salary}, hire date: {self.hire_date}, bonus: {self.bonus}"

    def calculate_manager_salary(self):
        tax_rate = 0.25  # 25% impozit și contribuții
        insurance_rate = 0.1  # 10% asigurări

        # Calculăm impozitul și contribuțiile
        total_tax = self.salary * tax_rate
        total_insurance = self.salary * insurance_rate

        # Calculăm salariul net
        net_salary = self.salary - total_tax - total_insurance
        return net_salary + (bonus/12)


managers_data = [
    (1, "maria", "hr", 6500, "2015-08-15", 1200),
    (2, "ion", "pr", 7500, "2017-08-15", 1400),
    (3, "elena", "it", 6000, "2018-08-15", 1100),
    (4, "vlad", "sales", 8800, "2005-08-15", 2500)
]

for mgr_data in managers_data:
    mgr_id, name, department, salary, hire_date, bonus = mgr_data
    manager = Manager(mgr_id, name, department, salary, hire_date, bonus)
    print(manager)

