conti = 0
contm = 0
contf = 0
while True:
    print("-"*30)
    print("{:^30}".format("Cadastre uma Pessoa"))
    print("-"*30)
    i = int(input("Idade: "))
    s = " "
    while s not in "mf":
        s = input("Sexo: [M/F] ").strip().lower()
    if i > 18:
        conti += 1
    if s == "m":
        contm += 1
    if s == "f" and i < 20:
        contf += 1
    print("-"*30)
    if input("Quer continuar? [S/N] ").strip().lower() == "n":
        break
print("-"*30)
print(f"Total de pessoas com mais de 18 anos: {conti}")
print(f"Ao todo temos {contm} homens cadastrados")
print(f"E temos {contf} mulheres com menos de 20 anos")