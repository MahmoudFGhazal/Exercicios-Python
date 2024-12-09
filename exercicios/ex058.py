from random import randint
c = randint(0, 10)
print(c)
print("Sou seu computador...")
print("Pensei em um número de 0 a 10")
print("Será que você consegue advinhar?")
n = int(input("Qual é o seu palpite? "))
cont = 1
while n != c:
    if n < c:
        print("Maior, tente novamente")
    else:
        print("Menor, tente novamente")
    n = int(input("Qual é o seu palpite? "))
    cont = cont + 1
print("Parabens, você acertou com {} tentativas".format(cont))

