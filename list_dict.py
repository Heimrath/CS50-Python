students = ["Hermione", "Harry", "Ron", "Draco"]

print(students[0])
print(students[1]) 
print(students[2])

for s in students[1]: # This will print each letter of the string
    print(s)

for s in students[1:]:  # This will print the string starting from the Students[1]
    print(s)

print("\n")

comidas = ["arroz", "feijão", "batata", "macarrão"]
for c in range(len(comidas)):
    print(c + 1, comidas[c])

print("\n")

# DICIONÁRIOS (TEMOS AS CHAVES (ESTUDANTES) E OS VALORES (CASAS))
students_2 = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Ron": "Grifinória",
    "Draco": "Sonserina"
}

for student in students_2:
    print(student, students_2[student], sep=": ")

print("\n")

# LISTA DE DICIONÁRIOS
students_3 = [
    {"name": "Hermione", "house": "Grifinória", "patronus": "Lontra"},
    {"name": "Harry", "house": "Grifinória", "patronus": "Cervo"},
    {"name": "Ron", "house": "Grifinória", "patronus": "Cachorro"},
    {"name": "Draco", "house": "Sonserina", "patronus": None}
]

for student in students_3:
    print(student["name"], student["house"], student["patronus"], sep=", ")
