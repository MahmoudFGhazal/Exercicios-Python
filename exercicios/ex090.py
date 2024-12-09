n = dict()
n["nome"] = input("Nome: ")
n["media"] = float(input(f"Media de {n["nome"]}: "))
if n["media"] < 6:
    n["situ"] = "Reprovado"
elif n["media"] < 7:
    n["situ"] = "Recuperação"
else:
    n["situ"] = "Aprovado"
print("-="*15)
print(f"Nome é igual a {n["nome"]}")
print(f"Media é igual a {n["media"]}")
print(f"A situação é igual a {n["situ"]}")

