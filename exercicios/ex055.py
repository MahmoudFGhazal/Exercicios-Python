m = 0
n = 0
for c in range(0, 5):
    p = float(input("Peso da {}º pessoa".format(c+1)))
    if p > m or c == 0:
        m = p
    if p < n or c == 0:
        n = p
print("O maior peso foi", m)
print("O menor peso foi", n)
