# Imprime todos os nomes, com uma linha de espaço entre eles
'''
with open("nomes.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
'''

# Imprime os nomes sem o espaço
'''
with open("nomes.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
'''

# Usa uma lista para imprimir os nomes em ordem alfabetica 
nomes = []
with open("nomes.txt", "r") as file:
    for line in file:
        nomes.append(line.strip())

for nome in sorted(nomes):
    print(f"Hello, {nome}")


