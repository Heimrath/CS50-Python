from hello2 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Matheus") == "hello, Matheus"