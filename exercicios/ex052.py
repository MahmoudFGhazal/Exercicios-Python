n = int(input("Digite um número: "))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print("\033[33m{}".format(c), end=" ")
        cont = cont + 1
    else:
        print("\033[31m{}".format(c), end=" ")
print("\n\033[mO número {} foi divisivel {} vezes".format(n, cont))
if cont > 2:
    print("Por isso ele não é primo")
else:
    print("Por isso ele é primo")