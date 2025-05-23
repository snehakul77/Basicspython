employees = [
    {"name": "Alice", "department": "HR", "salary": 50000, "experience": 5},
    {"name": "Bob", "department": "Engineering", "salary": 75000, "experience": 4},
    {"name": "Charlie", "department": "Marketing", "salary": 62000, "experience": 6},
    {"name": "David", "department": "Engineering", "salary": 68000, "experience": 3},
    {"name": "Eva", "department": "HR", "salary": 52000, "experience": 7},
    {"name": "Frank", "department": "Marketing", "salary": 61000, "experience": 2}
]

#sort employees by salaries and print top 3 highest paid employees
#sort_employees = sorted(employees, key=lambda employee: employee["experience"], reverse=True)
#print(sort_employees[:3])

#Group Employees by Department (Just List Their Names)

dept_employees = {}
for emp in employees:
    dept = emp["department"]
    name = emp["name"]
    #print(dept, name)
    print(dept_employees)
    if dept not in dept_employees:
        dept_employees[dept] = []
    dept_employees[dept].append(name)
print(dept_employees)
#for dept in dept_employees:
    #print(f" {dept} : {dept_employees["name"]}")





