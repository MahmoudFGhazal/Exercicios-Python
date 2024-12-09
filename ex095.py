n = dict()
r = list()
continuar = True
while continuar:
    n.clear()
    n["nome"] = input("Nome do jogador: ").title().strip()
    while True:
        p = int(input(f"Quantas partidas {n["nome"]} jogou? "))
        if p >= 0:
            break
        print("Numero de Partidas Invalidas")
    x = list()
    for c in range(1, p+1):
        while True:
            g = int(input(f"Quantos gols na partida {c}? "))
            if g >= 0:
                x.append(g)
                break
            print("Numero de gols Invalido")
    n["gols"] = x
    n["total"] = sum(x)
    r.append(n.copy())
    while True:
        e = input("Quer continuar? [S/N] ").strip()
        if e in "Nn":
            continuar = False
            break
        elif e in "Ss":
            break
        print("Opção Invalida")

r = sorted(r, key=lambda x: x["total"], reverse=True)
print("=-"*30)
print(f"{"Cod":<4}{"Nome":<15}{"Media":<15}total")
print("-"*50)
for c, i in enumerate(r):
    print(f"{c+1:>2}  ", end="")
    for k in i.values():
        print(f"{str(k):<15}", end="")
    print()
while True:
    c = int(input("Mostrar dados de qual jogador? (0 para sair) ")) - 1
    if c == -1:
       break
    print(f"-- Levantamento do Jogador {r[c]["nome"]}:")
    for cont, i in enumerate(r[c]["gols"]):
        print(f"    No jogo {cont+1} fez {i} gols.")
    print("-"*50)