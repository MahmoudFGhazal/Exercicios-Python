n = []
while True:
    p = int(input("Digite um valor: "))
    if p not in n:
        n.append(p)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! não vou adicionar!")

    if input("Quer continuar? [S/N] ").lower().strip() == "n":
        break
n.sort()
n = ", ".join(map(str, n))
print(f"Você digitou os valores {n}")
