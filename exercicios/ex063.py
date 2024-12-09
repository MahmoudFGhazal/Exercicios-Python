print("Sequencia de Fibonacci")
print("-"*30)
cont = int(input("Quantos termos você quer mostrar? "))
n = 0
r = 0
p = 1
print(n, end="")
while cont > 1:
    print(" -> {}".format(p), end="")
    n = r
    r = p
    p = r + n
    cont -= 1
print("\nFIM")