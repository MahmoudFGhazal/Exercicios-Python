from random import randint
c = int(input("Vou pensar em um núemro de 0 a 5\nTente adivinhar! "))
n = randint(0,5)
if c == n:
    print("Você acertou")
else:
    print("Você errou, eu pensei no {}".format(n))

