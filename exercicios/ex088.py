from random import randint
print("-"*30)
print(f"{"MEGA SENA":^30}")
print("-"*30)
n = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"{"Sorteando {} jogos".format(n):=^50}")
sorteio = []
for c in range(1, n+1):
    cont = 0
    print(f"Jogo {c}: ", end="")
    while True:
        l = randint(1, 60)
        if l not in sorteio:
            sorteio.append(l)
            cont += 1
        if cont >= 6:
            break
    print(sorteio)
    sorteio.clear()
print(f"{"Boa Sorte":=^50}")