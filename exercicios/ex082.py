n = []
pares = []
impar = []
while True:
    n.append(int(input("Digite um valor: ")))
    if n[-1] % 2 == 0:
        pares.append(n[-1])
    else:
        impar.append(n[-1])
    if input("Quer continuar? [S/N] ").lower().strip() == "n":
        break
n = ", ".join(map(str, n))
pares = ", ".join(map(str, pares))
impar = ", ".join(map(str, impar))
print(f"A lista completa é {n}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impar}")
