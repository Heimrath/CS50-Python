import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.dragon("Hello, " + sys.argv[1])