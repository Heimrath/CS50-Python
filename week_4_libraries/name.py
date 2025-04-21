# Passar argumentos pelo terminal usando sys argv

# argv[0] = o nome do programa "name.py" neste caso
# argv[1] = o que vem a seguir, e assim por diante

import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    sys.exit("Pouco argumentos foram inseridos")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)