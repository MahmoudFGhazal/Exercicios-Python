n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
maior = 0
for c in range(0, 3):
    for x in range(0, 3):
        n[x][c] = int(input(f"Digite para [{c}, {x}]: "))
        if n[x][c] % 2 == 0:
            par += n[x][c]
        if x == 2:
            soma += n[x][c]
        if n[x][c] > maior and c == 1 or maior == 0:
            maior = n[x][c]
print("-"*30)
for c in range(0,3):
    for x in range(0,3):
        print(f"[{n[x][c]:^5}]", end="")
    print()
print("-"*30)
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da terceira coluna é {soma}")
print(f"O maior valor da segunda linha é {maior}")
