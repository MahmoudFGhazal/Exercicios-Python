from random import randint
x = []
m = 0
n = 0
for c in range(0, 5):
    x.append(randint(0, 10))
    if c == 0 or m < x[c]:
        m = x[c]
    if c == 0 or n > x[c]:
        n = x[c]
p = ", ".join(map(str, x))
print(f"O valores sorteados foram {p}")
print(f"O maior número foi {m}")
print(f"O menor número foi {n}")
