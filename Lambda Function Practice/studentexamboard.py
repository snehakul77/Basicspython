students = [
    {"name": "Alice", "class": "10A", "math_score": 88, "science_score": 92, "english_score": 85},
    {"name": "Bob", "class": "10B", "math_score": 75, "science_score": 80, "english_score": 78},
    {"name": "Charlie", "class": "10A", "math_score": 90, "science_score": 87, "english_score": 93},
    {"name": "David", "class": "10B", "math_score": 64, "science_score": 70, "english_score": 68},
    {"name": "Eva", "class": "10A", "math_score": 95, "science_score": 91, "english_score": 89}
]

#Calculate total score (math + science + English) for each student and print their name with total
for student in students:
    score = student["math_score"] + student["science_score"] + student["english_score"]
    print(f"{student['name']}: {score}")
print("-----" *30)
#Find the topper (highest total score).
max_student = max(students, key=lambda student: student["math_score"] + student["science_score"] + student["english_score"])
print(max_student["name"])

#Group students by class

class_divide = {}
for student in students:
    division = student["class"]
    name = student["name"]
    if division not in class_divide:
        class_divide[division] = []
    class_divide[division].append(name)
print(class_divide)

# Sort students by English score (highest to lowest).

sort_engscore = sorted(students, key=lambda student: student["english_score"], reverse=True)
print("----Sorting by english score----")
print(sort_engscore)

#Filter students who scored above 90 in math.

math_toppers = [student for student in students if student["math_score"] >= 90]
print(math_toppers)