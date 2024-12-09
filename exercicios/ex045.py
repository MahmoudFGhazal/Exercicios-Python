from random import randint
c = ["pedra", "papel", "tesoura"]
p = int(input("1. Pedra\n2. Papel\n3. Tesoura\nEscolha: ")) - 1
if -1 < p < 3:
    x = randint(0,2)
    print("Você jogou {} e o robo jogou {}".format(c[p], c[x]))
    if p == x:
        print("Empate")
    elif p == 1 and x == 2 or p == 2 and x == 3 or p == 3 and x == 1:
        print("Perdeu")
    else:
        print("Ganhou")
else:
    print("Opção Invalida")
