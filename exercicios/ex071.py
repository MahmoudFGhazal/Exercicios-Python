print("-"*30)
print("{:^30}".format("Banco Arabe"))
print("-"*30)
n = int(input("Que valor você quer sacar? R$"))
c100 = n // 100
n %= 100
c50 = n // 50
n %= 50
c10 = n // 10
n %= 10
c5 = n // 5
n %= 5
c1 = n // 1
print(f"Total de {c100} cédulas de R100")
print(f"Total de {c50} cédulas de R50")
print(f"Total de {c10} cédulas de R10")
print(f"Total de {c5} cédulas de R5")
print(f"Total de {c1} cédulas de R1")
print("-"*30)
print(f"Volte sempre ao Banco Arabe! Tenha um Bom dia")