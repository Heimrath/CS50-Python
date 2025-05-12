import pytest
from calculadora import quadrado


# Neste caso vamos utilizar a ferramenta PyTest (python -m pytest) (automatiza nosso try e excepts)
'''
    assert quadrado(2) == 4
    assert quadrado(3) == 9
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9
    assert quadrado(0) == 0
'''

# Pytest não executa os outros testes ao encontrar o primeiro erro neste modelo que estava usando, para melhorar usamos funções

def test_positive():
    assert quadrado(2) == 4
    assert quadrado(3) == 9


def test_negative():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9


def test_zero():
    assert quadrado(0) == 0


def test_str():
    with pytest.raises(TypeError):
        quadrado("cat")