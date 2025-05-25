students = [
    {"name": "Alice", "class": "10A", "math_score": 88, "science_score": 92, "english_score": 85},
    {"name": "Bob", "class": "10B", "math_score": 75, "science_score": 80, "english_score": 78},
    {"name": "Charlie", "class": "10A", "math_score": 90, "science_score": 87, "english_score": 93},
    {"name": "David", "class": "10B", "math_score": 64, "science_score": 70, "english_score": 68},
    {"name": "Eva", "class": "10A", "math_score": 95, "science_score": 91, "english_score": 89}
]

#Add Total and Average Score to Each Student

for student in students:
    total = student["math_score"] + student["science_score"] + student["english_score"]
    student["total"] = total
    student["average"] = student["total"] / 3

for student in students:
    print(student)

#Group students by class
class_divide = {}
for student in students:
    cls = student["class"]
    if cls not in class_divide:
        class_divide[cls] = []
    class_divide[cls].append(student)
print(class_divide)
#Find topper of each class
for cls, student_list in class_divide.items():
    topper = max(student_list, key=lambda x: x['total'])
    print(f" Topper of class {cls}: {topper['name']}")

