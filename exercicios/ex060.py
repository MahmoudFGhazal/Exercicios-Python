n = int(input("Digite um número: "))
msg = "{}! = {}".format(n,n)
f = n
c = n - 1
while c > 0:
    msg = msg + "x {} ".format(c)
    f *= c
    c -= 1
msg = msg + "= {}".format(f)
print(msg)