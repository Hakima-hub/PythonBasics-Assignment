student = {
    "name": "Zakir",
    "age": 8,
    "marks": 90
}
#Update
student["marks"] = 96
#Add grade
student["grade"] = "A"

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
