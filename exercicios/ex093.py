n = dict()
n["nome"] = input("Nome do jogador: ").title()
p = int(input(f"Quantas partidas {n["nome"]} jogou? "))
x = list()
cont = 0
for c in range(1, p+1):
    x.append(int(input(f"Quantos gols na partida {c}? ")))
n["gols"] = x
n["total"] = sum(x)
print("=-"*30)
print(n)
print("=-"*30)
for c, i in n.items():
    print(f"O campo {c} tem o valor {i}")
print("=-"*30)
print(f"O jogador {n["nome"]} jogou {p} partidas")
for c, i in enumerate(n["gols"]):
    print(" "*5 + f"=> Na partida {c+1}, fez {i} gols")
print(f"Foi um total de {n["total"]} gols.")
