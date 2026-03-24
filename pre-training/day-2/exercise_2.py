students = [
    {"name": "Ali",   "subject": "Math",    "scores": [85, 90, 78]},
    {"name": "Sara",  "subject": "Science", "scores": [92, 88, 95]},
    {"name": "Ahmed", "subject": "Math",    "scores": [70, 65, 72]},
    {"name": "Zara",  "subject": "English", "scores": [60, 75, 68]},
    {"name": "Bilal", "subject": "Science", "scores": [80, 82, 79]},
]


def calculate_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return round(total / len(scores), 1)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def class_topper(students):
    topper = students[0]
    for student in students:
        if calculate_average(student["scores"]) > calculate_average(topper["scores"]):
            topper = student
    return topper


topper = class_topper(students)

sorted_students = sorted(students, key=lambda s: calculate_average(s["scores"]), reverse=True)

print(f"{'Name':<10} {'Subject':<10} {'Average':<10} {'Grade'}")
print("-" * 45)

for student in sorted_students:
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)
    tag = " TOP" if student["name"] == topper["name"] else ""
    print(f"{student['name']:<10} {student['subject']:<10} {avg:<10} {grade}{tag}")

print("-" * 45)
print(f"Class Topper: {topper['name']} with {calculate_average(topper['scores'])}")
