import uteis
p = float(input("Digite o preço: R$"))
m = uteis.moeda(p)
print(f"A metade de {m} é {uteis.metade(p, True)}")
print(f"O dobro de {m} é {uteis.dobro(p, True)}")
a = 5
print(f"Aumentando {a}%, temos {uteis.porcentagem(p, a, True)}")