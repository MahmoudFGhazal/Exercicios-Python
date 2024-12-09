def area(l, c):
    print(f"A area de um terreno {l}x{c} é de {l*c}m^2")


print(f"{"Controle de Terrenos":^30}")
print("-"*30)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)
