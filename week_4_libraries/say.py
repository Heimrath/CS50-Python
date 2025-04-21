import sys
from sayings import hey # do arquivo sayings importa o modulo hey

if len(sys.argv) == 2:
    hey(sys.argv[1])        # chamando o modulo hey