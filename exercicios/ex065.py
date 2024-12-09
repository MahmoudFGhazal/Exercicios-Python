cont = 0
s = 0
p = 0
m = 0
r = ""
while r != "N":
    n = int(input("Digite um número: "))
    if n > m or cont == 0:
        m = n
    if n < p or cont == 0:
        p = n
    cont += 1
    s += n
    r = input("Quer continuar? [S/N] ").upper().strip()
print("Você digitou {} números e a media foi {}".format(cont, s/cont))
print("O maior número foi {} e o menor foi {}".format(m, p))
