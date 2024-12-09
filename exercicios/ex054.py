from datetime import date
h = date.today().year
contm = 0
contn = 0
for c in range(0, 7):
    p = int(input("Em que ano a {}º nasceu? ".format(c+1)))
    if h - p >= 18:
        contm = contm + 1
    elif h - p < 18:
        contn = contn + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(contm))
print("Ao todo tivemos {} pessoas menores de idade".format(contn))
