s = 0
for c in range(1,7):
    n = int(input("Insira o {}º número: ".format(c)))
    if n % 2 == 0:
        s = s + n
print(s)
