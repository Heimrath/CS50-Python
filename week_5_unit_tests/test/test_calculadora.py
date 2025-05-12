from calculadora import quadrado


def main():
   test_quadrado()


def test_quadrado():

    # Maneira de testar, porem pode conter erros, no caso de 2 + 2 que continua sendo 4

    '''
    if quadrado(2) != 4:
        print("2 ao quadrado não é 4")
    if quadrado(3) != 9:
        print("3 ao quadrado não é 9")
    '''

    # Com a palavra -> assert <- estamos afirmando que tal coisa é verdadeira ou falsa, 
    # retorna um valor -> AssertionError <- caso nossa afirmação esteja errada

    assert quadrado(2) == 4
    assert quadrado(3) == 9

    # Podemos melhorar usando try e except

    '''
    try:
        assert quadrado(2) == 4
    except AssertionError:
        print("2 ao quadrado não foi  4") # Apenas uma mensagem indicando que nosso programa não retornou o valor esperado, no caso 4
    try:
        assert quadrado(3) == 9
    except AssertionError:
        print("3 ao quadrado não foi 9")
    try:
        assert quadrado(-2) == 4
    except AssertionError:
        print("-2 ao quadrado não foi 4")
    try:
        assert quadrado(-3) == 9
    except AssertionError:
        print("-3 ao quadrado não foi 9")
    try:
        assert quadrado(0) == 0
    except AssertionError:
        print("0 ao quadrado não foi 0")
    '''

    # Entretanto, ninguém vai querer escrever dezenas de código para testar uma função de apenas 2 linhas
    # Neste caso vamos utilizar a ferramenta PyTest (python -m pytest) que irá automatizar nosso try e except (no arquivo test_calculadora_pytest)


if __name__ == "__main__":
    main()