from random import randint
cont = 0
pp = 0
pc = 0
while cont < 3:
    print("=-"*15)
    print("Vamos jogar par ou impar! Melhor de 3")
    print("=-" * 15)
    c = randint(0, 10)
    n = int(input("Diga um valor: "))
    e = ""
    while e not in "pi":
        e = input("Par ou Impar? [P/I] ").lower().strip()
    if e == "p":
        if n + c % 2 == 0:
            print(f"Você jogou {n} e o computador {c}. Você Ganhou!")
            pp += 1
        else:
            print(f"Você jogou {n} e o computador {c}. Você Perdeu!")
            pc += 1
    elif e == "i":
        if n + c % 2 != 0:
            print(f"Você jogou {n} e o computador {c}. Você Ganhou!")
            pp += 1
        else:
            print(f"Você jogou {n} e o computador {c}. Você Perdeu!")
            pc += 1
    cont += 1
if pp > pc:
    print("Parabens, você Ganhou da Maquina!!!")
else:
    print("GAME OVER!!!")
