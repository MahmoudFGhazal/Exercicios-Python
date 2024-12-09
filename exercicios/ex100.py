from random import randint


def sorteio():
    x = list()
    for c in range(0, 5):
        x.append(randint(0, 10))
        print(x[c], end=" ")
    print()
    return x


def soma(num):
    n = 0
    for c in num:
        if c % 2 == 0:
            n += c
    return n


num = sorteio()
n = soma(num)
print(n)
