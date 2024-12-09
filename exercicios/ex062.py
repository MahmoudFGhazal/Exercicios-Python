print("Gerador de PA")
print("=================")
n = int(input("Primeiro termo: "))
r = int(input("Razão: "))
cont = 0
cont2 = 9
while cont <= cont2:
    print("{} -> ".format(n), end="")
    n += r
    cont += 1
    if cont > cont2:
        print("PAUSA")
        cont2 += int(input("Quantos termos quer mostrar a mais? "))

print("A progressão foi finalizada com {} termos mostrados".format(cont))
