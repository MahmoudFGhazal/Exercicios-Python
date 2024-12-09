from random import randint
from operator import itemgetter
n = dict()
ranking = dict()
for c in range(1, 5):
    n[f"jogador{c}"] = randint(1, 6)
    print(f"jogafor{c} tirou {n[f"jogador{c}"]} no dado.")
ranking = sorted(n.items(), key=itemgetter(1), reverse=True)
print("-="*15)
print(f"{"== RAKING DOS JOGADORES ==":^30}")
for c, v in enumerate(ranking):
    print(f"{c+1}º lugar: {v[0]} com {v[1]}")