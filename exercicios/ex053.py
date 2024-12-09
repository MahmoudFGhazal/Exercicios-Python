n = input("Digite uma palavra: ").strip().upper()
p = "".join(n.split())
i = ""
for c in range(len(n) - 1, -1, -1):
    i = i + p[c]
print("O inverso de {} é {}".format(n, i))
if i == n:
    print("É palindromo")
else:
    print("Não é palindromo")
