x =  int(input("Qual é o valor de x? "))
y =  int(input("Qual é o valor de  y? "))

if x < y:
    print("x é menor do que y")
elif x > y:
    print("x é maior do que y")
else:
    print("x é igual a y")

# if x < y or x > y:
#     print("x não é igual a y")
# else:
#     print("x é igual a y")

if x != y:
    print("x não é igual a y")
else:
    print("x é igual a y")

nota = int(input("Qual é a nota do aluno? (0 - 100) "))

# version 1 --------------------------------------

if nota >= 90 and nota <= 100:
    print("Nota: A")
elif nota >= 80 and nota < 90:
    print("Nota: B")
elif nota >= 70 and nota < 80:
    print("Nota: C")
elif nota >= 60 and nota < 70:
    print("Nota: D")
else: 
    print("Nota: F")

# version 2 --------------------------------------

if 90 <= nota <= 100:
    print("Nota: A")
elif 80 <= nota < 90:
    print("Nota: B")
elif 70 <= nota < 80:
    print("Nota: C")
elif 60 <= nota < 70:
    print("Nota: D")
else: 
    print("Nota: F")

# version 3 --------------------------------------

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
elif nota >= 60:
    print("Nota: D")
else:
    print("Nota: F")



def par_impar(n):
    return n % 2 == 0       # Forma compacta parar retornar True se n é par e False se n é ímpar
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

numero = int(input("Digite um número: "))
if par_impar(numero):       # se a função retornar True, entra no if
    print("O número é par")
else:                       # se a função retornar False, entra no else
    print("O número é ímpar")