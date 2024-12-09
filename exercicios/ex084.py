n = []
p = []
main = []
maior = menor = 0
while True:
    n.append(input("Nome: "))
    n.append(float(input("Peso: ")))
    if len(p) == 0:
        maior = menor = n[1]
    else:
        if n[1] > maior:
            maior = n[1]
        if n[1] < menor:
            menor = n[1]
    p.append(n[:])
    n.clear()

    if input("Quer continuar? [S/N] ").lower().strip() == "n":
        break

print("-"*30)
print(f"Ao todo, você cadastrou {len(p)} pessoas.")
nomes = ""
for m in p:
    if m[1] == maior:
        nomes += m[0] + ", "
print(f"O maior peso foi de {maior}Kg. Peso de {nomes[:-2]}")
nomes = ""
for m in p:
    if m[1] == menor:
        nomes += m[0] + ", "
print(f"O menor peso foi de {menor}Kg. Peso de {nomes[:-2]}")