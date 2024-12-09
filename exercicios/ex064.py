cont = 0
s = 0
while True:
    n = input("Digite um número [sair para parar]: ").lower().strip()
    if not n.isnumeric():
        if n == 'sair':
            break
        else:
            print("Opção Invalida")
            continue
    n = int(n)
    s += n
    cont += 1
print("Você digitou {} números e a soma foi {}".format(cont,s))


