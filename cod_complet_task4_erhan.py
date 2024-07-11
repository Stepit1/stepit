departments = [
    {"dept_id": 1, "name": "HR"},
    {"dept_id": 2, "name": "Contabilitate"},
    {"dept_id": 3, "name": "Legal"},
    {"dept_id": 4, "name": "Finance"},
    {"dept_id": 5, "name": "Marketing"}
    ]
    
employee_departments = [
    {"emp_id": 1, "dept_id": 1},
    {"emp_id": 2, "dept_id": 2},
    {"emp_id": 3, "dept_id": 3},
    {"emp_id": 4, "dept_id": 4},
    {"emp_id": 5, "dept_id": 5}
    ]
    
manager_departments = [
    {"mgr_id": 1, "dept_id": 1},
    {"mgr_id": 2, "dept_id": 2},
    {"mgr_id": 3, "dept_id": 3},
    {"mgr_id": 4, "dept_id": 4},
    {"mgr_id": 5, "dept_id": 5}
    ]

def show_departments(departments):
    print("Departments Table: ")
    for dept in departments:
        return f"Department ID: {dept['dept_id']}, Name: {dept['name']}"
        
def show_employee_departments(employee_departments):
    print("Employee Departments Table: ")
    for emp_dept in employee_departments:
        return f"Employee ID: {emp_dept['emp_id']}, Department ID: {emp_dept['dept_id']}"
        
def show_manager_departments(manager_departments):
    print("Manager Departments Table: ")
    for mgr_dept in manager_departments:
        return f"Manager ID: {mgr_dept['mgr_id']}, Department ID: {mgr_dept['dept_id']}"

show_departments(departments)
show_employee_departments(employee_departments)
show_manager_departments(manager_departments)
