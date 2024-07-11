import pandas as pd
import os


class Employee:
    def __init__(self, emp_id, name, company, position, salary, hire_date, department):
        self.emp_id = emp_id
        self.name = name
        self.company = company
        self.position = position
        self.salary = salary
        self.hire_date = hire_date
        self.department = department

    def to_dict(self):
        return {
            'emp_id': self.emp_id,
            'Name': self.name,
            'Company': self.company,
            'Position': self.position,
            'Salary': self.salary,
            'Hire_Date': self.hire_date,
            'Department': self.department
        }


class CompanyDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return [emp.to_dict() for emp in self.employees]


class Updates_Emp:
    def __init__(self):
        self.emp_salary = []

    def add_new_salary(self, emp_id, new_salary):
        self.emp_salary.append((emp_id, new_salary))

    def get_emp_salaries(self):
        return self.emp_salary


class Update_Manager_Bonus:
    def __init__(self):
        self.mgr_bonus = []

    def add_new_bonus(self, mgr_id, new_mgr_bonus):
        self.mgr_bonus.append((mgr_id, new_mgr_bonus))

    def get_mgr_bonuses(self):
        return self.mgr_bonus


class Assign_employee_to_project:
    def __init__(self):
        self.emp_project = []

    def add_new_project(self, emp_id, new_project):
        self.emp_project.append((emp_id, new_project))

    def get_emp_projects(self):
        return self.emp_project


class Assign_employee_to_department:
    def __init__(self):
        self.department = []

    def add_new_dep(self, emp_id, new_dep):
        self.department.append((emp_id, new_dep))

    def get_emp_departments(self):
        return self.department


def initialize_csv_database(database):
    employees = database.get_employees()
    df = pd.DataFrame(employees)
    df.to_csv('company_data.csv', index=False)
    print("Baza de date inițială a fost creată în fișierul company_data.csv")


def update_csv_database(emp_updates, mgr_updates, emp_project_assignments, emp_department_assignments):
    csv_file = 'company_data.csv'

    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file)
            if df.empty:
                raise pd.errors.EmptyDataError
        except (pd.errors.EmptyDataError, pd.errors.ParserError):
            df = pd.DataFrame(
                columns=['emp_id', 'Name', 'Company', 'Position', 'Salary', 'Hire_Date', 'Department', 'Bonus',
                         'Project'])
    else:
        df = pd.DataFrame(
            columns=['emp_id', 'Name', 'Company', 'Position', 'Salary', 'Hire_Date', 'Department', 'Bonus', 'Project'])

    # Actualizează salariile angajaților
    for emp_id, new_salary in emp_updates.get_emp_salaries():
        df.loc[df['emp_id'] == emp_id, 'Salary'] = new_salary

    # Actualizează bonusurile managerilor
    for mgr_id, new_bonus in mgr_updates.get_mgr_bonuses():
        df.loc[df['emp_id'] == mgr_id, 'Bonus'] = new_bonus

    # Actualizează proiectele angajaților
    for emp_id, new_project in emp_project_assignments.get_emp_projects():
        df.loc[df['emp_id'] == emp_id, 'Project'] = new_project

    # Actualizează departamentele angajaților
    for emp_id, new_dep in emp_department_assignments.get_emp_departments():
        df.loc[df['emp_id'] == emp_id, 'Department'] = new_dep

    df.to_csv(csv_file, index=False)
    print("Datele au fost actualizate în fișierul company_data.csv")


if __name__ == "__main__":
    database = CompanyDatabase()
    emp_updates = Updates_Emp()
    mgr_updates = Update_Manager_Bonus()
    emp_project_assignments = Assign_employee_to_project()
    emp_department_assignments = Assign_employee_to_department()

    employees_data = [
        Employee(1, "John Doe", "TechCorp", "Manager", 75000, "2015-04-22", "IT"),
        Employee(2, "Jane Smith", "HealthInc", "Senior Developer", 95000, "2018-07-15", "R&D"),
        Employee(3, "Jim Brown", "EduWorld", "Junior Developer", 45000, "2020-01-10", "IT"),
        Employee(4, "Emily White", "FinServe", "Sales Representative", 50000, "2017-05-30", "Sales"),
        Employee(5, "Michael Green", "AutoMotive", "HR Specialist", 55000, "2016-09-25", "HR"),
        Employee(6, "Jessica Black", "Foodies", "Accountant", 60000, "2019-03-11", "Finance"),
        Employee(7, "David Blue", "MediCare", "Data Analyst", 70000, "2014-11-05", "R&D"),
        Employee(8, "Laura Red", "BuildIt", "Product Manager", 85000, "2017-08-19", "Marketing"),
        Employee(9, "Chris Yellow", "TravelNow", "Marketing Specialist", 62000, "2016-02-27", "Marketing"),
        Employee(10, "Patricia Purple", "RetailHub", "Support Engineer", 58000, "2019-10-03", "Support")
    ]

    for employee in employees_data:
        database.add_employee(employee)

    # Inițializează baza de date cu angajați
    initialize_csv_database(database)

    # Adaugă update-uri și alte informații
    emp_updates.add_new_salary(1, 80000)
    mgr_updates.add_new_bonus(1, 10000)
    emp_project_assignments.add_new_project(1, 'Project X')
    emp_department_assignments.add_new_dep(1, 'IT')

    # Actualizează baza de date CSV
    update_csv_database(emp_updates, mgr_updates, emp_project_assignments, emp_department_assignments)