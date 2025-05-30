nome = input("Qual o seu nome? ")


# Abre ou cria o arquivo, "w" escreve, porém reescreve, podendo apagar o conteudo inicial
# file = open("nomes.txt", "w") 

# "a" = append, adiciona no arquivo a medida que escrevemos, sem apagar
# file = open("names.txt", "a") 

# Escreve no arquivo  
# file.write(f"{nome}\n")

# Fecha o arquivo 
# file.close() 

# Com "with" não precisamos usar o file.close()
with open("nomes.txt", "a") as file:
    file.write(f"{nome}\n")