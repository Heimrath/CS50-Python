import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

resposta = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]) # o usuario deve inserir o nome da banda no terminal
print(json.dumps(resposta.json(), indent=2)) # imprime no formato de dicionario python

obj = resposta.json()

for resultado in obj["results"]: # results é uma lista, que contem um ou mais dicionarios (especificado em "limit"), neste temos uma chave chamada trackName em que seus valores sao os nomes das musicas
    print(resultado["trackName"]) # imprime todas os valores das chaves trackName
