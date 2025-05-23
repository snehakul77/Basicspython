employees = [
    {"name": "Alice", "department": "HR", "salary": 50000, "experience": 5},
    {"name": "Bob", "department": "Engineering", "salary": 75000, "experience": 4},
    {"name": "Charlie", "department": "Marketing", "salary": 62000, "experience": 6},
    {"name": "David", "department": "Engineering", "salary": 68000, "experience": 3},
    {"name": "Eva", "department": "HR", "salary": 52000, "experience": 7},
    {"name": "Frank", "department": "Marketing", "salary": 61000, "experience": 2}
]

#Sort employees by experience most to least

#sort_employees = sorted(employees, key=lambda employee: employee["experience"], reverse=True)
#for employee in sort_employees:
#    print(employee)

#Find employee with highest salary in engineering department

#sort_depart= sorted(employees, key=lambda employee: (employee["department"],employee["salary"]))
#for employee in sort_depart:
#    if employee["department"] == "Engineering":
#        highestsalary = employee["salary"]
#        print(f"The highest salary is {employee['name']}: {employee['department']} {highestsalary}")
#print("----" *30)


#Print a list of employees who have more than 5 years of experience, and sort that list by salary (lowest to highest).

experienced_employees = [emp for emp in employees if emp["experience"] >= 5]
#for emp in experienced_employees:
    #print(emp)

sort_exp = sorted(experienced_employees, key=lambda emp: emp["salary"])
for emp in sort_exp:
    print(f" {emp['name']} {emp['experience']} {emp['salary']}")


