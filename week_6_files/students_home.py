import csv

students = []

with open("students_home.csv") as file:
    reader = csv.DictReader(file) # Le a primeira linha dos arquivo CSV para determinar o nome das chaves do dicionario 
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]): # Ordem alfabetica 
    print(f"{student['name']} is in {student['home']}")
