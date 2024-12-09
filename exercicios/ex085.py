p = [[], []]
for c in range(1,8):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        p[0].append(n)
    else:
        p[1].append(n)
p[0].sort()
p[1].sort()
t = p[0] + p[1]
t.sort()
t = ", ".join(map(str, t))
p[0] = ", ".join(map(str, p[0]))
p[1] = ", ".join(map(str, p[1]))
print(f"Todos os valores: {t}")
print(f"Os valores pares digitados foram: {p[0]}")
print(f"Os valores pares digitados foram: {p[1]}")
