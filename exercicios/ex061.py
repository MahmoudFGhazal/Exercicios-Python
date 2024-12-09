print("Gerador de PA")
print("=================")
n = int(input("Primeiro termo: "))
r = int(input("Razão: "))
p = n
while n < r*10+p:
    print("{} -> ".format(n), end="")
    n += r
print("FIM")
