# 6.Alexandru Dirzu - Implementarea funcțiilor de actualizare a bazei de date
# Descriere:
#
# Implementarea unei funcții update_employee_salary pentru a actualiza salariul unui angajat pe baza emp_id.
# Implementarea unei funcții update_manager_bonus pentru a actualiza bonusul unui manager pe baza mgr_id.
# Implementarea unei funcții assign_employee_to_project pentru a asigna un angajat la un proiect.
# Implementarea unei funcții assign_employee_to_department pentru a asigna un angajat la un departament.



class Updates_Emp:
    def __init__(self):
        self.emp_salary = []
    def add_new_salary(self, new_salary):
        self.emp_salary.append(new_salary)
    def __repr__(self):
        return f"New Salary: {self.emp_salary}"

class Update_Manager_Bonus:
    def __init__(self):
        self.mgr_bonus = []
    def add_new_bonus(self, new_mgr_bonus):
        self.mgr_bonus.append(new_mgr_bonus)
    def __repr__(self):
        return f"New Manager Bonus is: {self.mgr_bonus}"

class Assign_employee_to_project:
    def __init__(self):
        self.emp_project = []
    def add_new_project(self, new_project):
        self.emp_project.append(new_project)
    def __repr__(self):
        return f"Employees project are: {self.emp_project}"

class Assign_employee_to_department:
    def __init__(self):
        self.department = []
    def add_new_dep(self, new_dep):
        self.department.append(new_dep)
    def __repr__(self):
        return f"Your new deparment is: {self.department}"
    


