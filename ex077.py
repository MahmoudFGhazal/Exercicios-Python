palavra = ("aprender", "jogar", "bola", "neymar", "messi")
for c in palavra:
    print(f"Na palabra {c.title()} temos ", end="")
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
    print("")