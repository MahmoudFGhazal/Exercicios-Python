n = []
par = ""
for c in range(0, 4):
    n.append(int(input(f"Digite o {c+1}º número: ")))
    if n[c] % 2 == 0:
        par = par + str(n[c]) + " "
p = ", ".join(map(str, n))
print(f"Você digitou os valores {p}")
print(f"O valor 9 apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"O valor 3 apareceu na {n.index(3) + 1}º posição")
else:
    print("O número tres não aparece")
par = ", ".join(par.split())
print(f"O números pares são {par}")
