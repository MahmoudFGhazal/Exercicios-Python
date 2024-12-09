n = input("Digite uma expressão: ")
cont = 0
for d in range(0, len(n)):
    if n[d] in "(":
        cont += 1
    elif n[d] in ")":
        cont -= 1
print("Sua expressão está correta" if cont == 0 else "Sua expressão não está correta")
