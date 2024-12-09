n = []
for c in range(0, 5):
    p = int(input("Digite um valor: "))
    if c == 0 or p > n[-1]:
        n.append(p)
        print("Adicionado ao final da lista")
    else:
        for d in range(0, len(n)):
            if p < n[d]:
                n.insert(d, p)
                print(f"Adicionado na posição {d} da lista")
                break

n = ", ".join(map(str, n))
print(f"Lista: {n}")