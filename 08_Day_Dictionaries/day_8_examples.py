dog = {}

dog["name"] = "lucky"
dog["legs"] = 4
dog["age"] = 28
dog["breed"] = True

student = {
    "first_name": "Sinancan",
    "last_name": "Sevinç",
    "Gender": "Male",
    "Married": False,
    "Age": 24,
    "City": 34,
    "Country":"Turkey",
    "Skills":['C#','Python','.NET']
}

print(f"Dict length is: {len(student)}")
print(type(student["Skills"]))

student["Skills"].append("Django")
student["Skills"].append("SQL")
print(student["Skills"])

print(student.keys())
print(student.values())

new_list = student.items()

student.pop("Country")
print(student)
del student
print(student)