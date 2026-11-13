import csv

students = [
    ["ST001", "Computer Science", 200, 85, 78],
    ["ST002", "Cyber Security", 200, 90, 82],
    ["ST003", "Software Engineering", 100, 75, 68],
    ["ST004", "Computer Science", 300, 80, 75],
    ["ST005", "Information Technology", 200, 70, 65],
    ["ST006", "Cyber Security", 100, 95, 88],
    ["ST007", "Software Engineering", 300, 88, 80],
    ["ST008", "Computer Science", 100, 60, 55],
    ["ST009", "Information Technology", 300, 92, 85],
    ["ST010", "Cyber Security", 200, 78, 72],
    ["ST011", "Computer Science", 200, 89, 91],
    ["ST012", "Software Engineering", 100, 82, 76],
    ["ST013", "Information Technology", 200, 65, 60],
    ["ST014", "Cyber Security", 300, 86, 79],
    ["ST015", "Computer Science", 300, 94, 90]
]

headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully!")
