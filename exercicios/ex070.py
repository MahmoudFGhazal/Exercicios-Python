s = 0
contf = 0
contm = 0
print("-"*30)
print("{:^30}".format("Loja Super Batatão"))
print("-"*30)
while True:
    i = input("Nome do Produto: ").strip().title()
    n = float(input("Preço: R$ "))
    if s == 0 or contm > n:
        contm = n
        nome = i
    s += n
    if n > 1000:
        contf += 1
    if input("Quer continuar? [S/N] ").strip().lower() == "n":
        break
print("-"*30)
print(f"O total da compra foi R${s}")
print(f"Temos {contf} produtos custando mais de R$1000")
print(f"O produto mais barato foi {nome} que custou R${contm}")
