r = list()
p = dict()
continuar = True
media = 0
h = ""
while continuar:
    p.clear()
    p["nome"] = input("Nome: ").strip().title()
    while True:
        s = input("Sexo: [M/F] ").strip().upper()
        if s in "MF":
            p["sexo"] = s
            if s == "F":
                h += p["nome"] + " e "
            break
        print("Opção Invalida")
    while True:
        i = int(input("Idade: "))
        if 0 < i < 140:
            media += i
            p["idade"] = i
            break
        print("Idade Invalida")
    r.append(p.copy())
    while True:
        e = input("Quer continuar? [S/N] ").strip()
        if e in "Nn":
            continuar = False
            break
        elif e in "Ss":
            break
        print("Opção Invalida")
print("-="*30)
print(f"Ao todo temos {len(r)} pessoas cadastradas.")
media /= len(r)
print(f"A media de idade é de {media}")
print(f"As mulheres cadastradas foram {h[:-3]}")
h = ""
print(f"Lista das pessoas que estão acima da media de idade:")
for c in r:
    if c["idade"] > media:
        for k, v in c.items():
            print(f"{k} = {v}; ", end="")
        print()
print("ENCERRADO")