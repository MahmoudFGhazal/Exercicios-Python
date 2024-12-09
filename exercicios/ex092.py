from datetime import datetime
n = dict()
n["nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
n["idade"] = datetime.now().year - nasc
n["ctps"] = int(input("Carteira de trabalho (0 se não tiver): "))
if n["ctps"] != 0:
    n["contratação"] = int(input("Ano de contratação: "))
    n["salario"] = "R$" + input("Salario: R$")
    n["aposentadoria"] = n["contratação"] + 35 - nasc
else:
    del n["ctps"]
print("-="*15)
for c, i in n.items():
    print(f"{c.title()} é igual a {i}")
