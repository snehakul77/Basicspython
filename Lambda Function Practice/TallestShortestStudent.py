students = [
    {"name": "Alice", "height": 165},
    {"name": "Bob", "height": 172},
    {"name": "Charlie", "height": 158},
    {"name": "David", "height": 180},
    {"name": "Eva", "height": 170}
]

tallestStudent = max(students, key=lambda student: student["height"])
ShortestStudent = min(students, key=lambda student: student["height"])

print(f"TallestStudent: {tallestStudent['name']} ({tallestStudent['height']}cm)")
print(f"ShortestStudent: {ShortestStudent['name']} ({ShortestStudent['height']}cm)")

