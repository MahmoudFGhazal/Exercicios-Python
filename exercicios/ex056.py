m = 0
mi = 0
cont = 0
for c in range(0, 4):
    print("----- {}º Pessoa -----".format(c+1))
    n = input("Nome: ").title()
    i = int(input("Idade: "))
    s = input("Sexo [M/F]: ").upper()
    m = m + i
    if mi < i and s == "M":
        mi = i
        mn = n
    if s == "F" and i <= 20:
        cont = cont + 1
msg = "A média de idade do grupo é de {}\n".format(m/4)
msg = msg + "O homem mais velho tem {} anos e se chama {}\n".format(mi, mn)
msg = msg + "Ao todo são {} mulheres com menos de 20 anos".format(cont)
print(msg)
