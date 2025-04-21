def main():
    hey("World")
    bye("World")

def hey(name):
    print(f"Hey {name}")

def bye(name):
    print(f"Goodbye {name}")

if __name__ == "__main__":  # serve para que ao ser usado, como no arquivo "say", a funcao main nao seja executada
    main()                  # __name__ == "__main__" se refere ao nome do arquivo chamado na execucao. Portanto, se nao for "sayings", nao sera executado