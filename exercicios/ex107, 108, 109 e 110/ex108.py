from uteis import metade, dobro, porcentagem, moeda
p = float(input("Digite o preço: R$"))
m = moeda(p)
print(f"A metade de {m} é {moeda(metade(p))}")
print(f"O dobro de {m} é {moeda(dobro(p))}")
a = 5
print(f"Aumentando {a}%, temos {moeda(porcentagem(p, a))}")
