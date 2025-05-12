def main():
    x = int(input("Qual o valor de x? "))
    print(f"{x} ao quadrado é igual a", quadrado(x))


def quadrado(n): 
    # return n * n # Maneira correta, porem para testar nossos testes vamos modificar 
    return n * n 

if __name__ == "__main__":
    main()