import random # Importar a biblioteca inteira 
from random import choice as ch # Maneira de importar um metodo apenas de uma biblioteca

import statistics

coin = ch(["Heads", "Tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack","Queens","King"]
random.shuffle(cards)
for card in cards:
    print(card)

print(statistics.mean([100, 90]))