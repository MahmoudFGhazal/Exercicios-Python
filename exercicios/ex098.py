def contagem(t, i, f):
    print("-="*30)
    print(f"Contagem de {i} até {f} de {t} em {t}")
    p = 1
    if i > f:
        p = -1
    t *= p
    for c in range(i, f+p, t):
        print(c, end=" ")
    print("FIM!")


contagem(1, 1, 10)
contagem(2, 10, 0)
i = int(input(f"{"Inicio: ":<7}"))
f = int(input(f"{"Fim: ":<7}"))
p = int(input(f"{"Passo: ":<7}"))
contagem(p, i, f)
