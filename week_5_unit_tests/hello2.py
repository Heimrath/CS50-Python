def main():
    name = input("Qual seu nome? ")
    print(hello(name))


def hello(to="world"):
    # Para que possamos testar, deve-se retornar um valor, o que não acontece com o print
    # por isso substituimos para a seguinte maneira, e utilizando o print no main
    return f"hello, {to}"


if __name__ == "__main__":
    main()