n = []
m = 0
s = 0
maior = ""
menor = ""
for c in range(0, 5):
    n.append(int(input(f"Digite o {c+1}º número: ")))
    if c == 0 or n[c] > m:
        m = n[c]
        maior = str(c+1)
    elif n[c] == m:
        maior += f" e {c+1}"
    if c == 0 or n[c] < s:
        s = n[c]
        menor = str(c+1)
    elif n[c] == s:
        menor += f" e {c+1}"
p = ", ".join(map(str, n))
print(f"Você digitou os valores {p}")
print(f"O maior valor digitado foi {m} nas posições {maior}")
print(f"O menor valor digitado foi {s} nas posições {menor}")
