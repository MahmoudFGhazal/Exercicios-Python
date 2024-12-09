n = []
while True:
    n.append(int(input("Digite um valor: ")))
    if input("Quer continuar? [S/N] ").lower().strip() == "n":
        break
print(f"Você digitou {len(n)} elementos")
n.sort(reverse=True)
n = ", ".join(map(str, n))
print(f"Os valores em ordem decrescente são {n}")
print("O valor 5 faz parte da lista" if "5" in n else "O valor 5 não faz parte da lista")