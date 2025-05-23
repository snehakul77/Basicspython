#We have a list of students, and for each student, there is a list of their grades in different subjects (e.g., Math, Science, and English). We want to calculate:

#Calculate The average score for each student.

#Display the highest and lowest of each student score

#Display the complete details for every student.

students_scores = [
    {"name": "Alice", "scores": [85, 90, 78]},   # Alice's scores
    {"name": "Bob", "scores": [92, 88, 84]},     # Bob's scores
    {"name": "Charlie", "scores": [76, 81, 89]}, # Charlie's scores
    {"name": "David", "scores": [88, 91, 95]},   # David's scores
]

#print(students_scores[3]["scores"])

subjects = ["Math","Science", "English"]

def calaverage(scores):
    return sum(scores) / len(scores)

def gethighestlowest(scores):
    highest = max(scores)
    lowest = min(scores)
    return highest, lowest

def displaystudentdetails(student):
    average = calaverage(student["scores"])
    high, low = gethighestlowest(student["scores"])
    print(f"Student name: {student['name']}")
    print(f"Averahead score: {average:.2f}")
    print(f"Highest score: {high:.2f}")
    print(f"Lowest score: {low:.2f}")
    print("--"*15)

print("Student Details")
for student in students_scores:
    displaystudentdetails(student)
