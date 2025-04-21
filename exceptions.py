def main():
    valor = obter_inteiro("Qual é o valor de x? ")
    print(f"x = {valor} \n")


def obter_inteiro(mensagem):
    while True:
        try:
            return int(input("\n" + mensagem))
            # return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

main()

while True:    
    try:
        opcao = int(input("Escolha uma opção:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\nOpção: "))
    except ValueError:
        print("Opção inválida. Por favor, insira um número inteiro.")
    else:
        if 0 <= opcao <= 4:
            print(f"Você escolheu a opção: {opcao}\n")
            if opcao == 0:
                break