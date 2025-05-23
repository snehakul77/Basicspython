employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "Engineering", "salary": 75000},
    {"name": "Charlie", "department": "Marketing", "salary": 62000},
    {"name": "David", "department": "Engineering", "salary": 68000},
    {"name": "Eva", "department": "HR", "salary": 52000}
]

#Sort the employees by salary (lowest to highest).

sorted_employees = sorted(employees, key=lambda employee: employee["salary"])
for employee in sorted_employees:
    print(f" {employee['name']} {employee['department']} {employee['salary']}")

#Sort the employees by name (alphabetical order).

name_sort= sorted(employees, key=lambda employee: employee["name"])
for employee in name_sort:
    print(employee["name"])

#Sort the employees by department, then salary (within each department, lowest salary first).

sort_department = sorted(employees, key=lambda employee: (employee["department"], employee["salary"]))
#print(sort_department)
for employee in sort_department:
   if employee["department"] == "HR":
       print(f" {employee['name']}: {employee['department']} {employee['salary']}")
   elif employee["department"] == "Engineering":
       print(f" {employee['name']}: {employee['department']} {employee['salary']}")
   else:
       print(f" {employee['name']}: {employee['department']} {employee['salary']}")
