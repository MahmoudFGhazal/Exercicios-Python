n = float(input('Digite um número: '))
p = float(input('Digite outro número: '))
z = float(input('Digite outro número: '))

l = n
if p < n and p < z:
    l = p
if z < p and z < n:
    l = z

m = n
if p > n and p > z:
    m = p
if z > n and z > p:
    m = z

print('O menor número foi {}\nO maior número foi {}'.format(l,m))
