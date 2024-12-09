p = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
for c in range(p, p + 10 * r, r):
    print("{} ->".format(c), end=" ")
print("Acabou")