import random
a = input("Insira o nome de um aluno ")
b = input("Insira o nome de um aluno ")
c = input("Insira o nome de um aluno ")
d = input("Insira o nome de um aluno ")
lista = [a, b, c, d]
random.shuffle(lista)
print("A ordem de apresentação\n{}".format(lista))
