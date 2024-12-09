from uteis import metade, dobro, porcentagem
p = float(input("Digite o preço: R$"))
print(f"A metade de R${p} é {metade(p)}")
print(f"O dobro de R${p} é {dobro(p)}")
a = 5
print(f"Aumentando {a}%, temos {porcentagem(p, a)}")
