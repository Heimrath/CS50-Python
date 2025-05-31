students = []

with open("students_house.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


# Funcao que foi substituida por -> lambda
def get_name(student):
    return student["name"]

for student in sorted(students, key=lambda student: student["name"]): # Ordem alfabetica 
    print(f"{student['name']} is in {student['house']}")
