msg = ("Lapis", 1.75, "Borracha", 2, "Caderno", 15.9)
print("-"*50)
print(f"{"Listagem de Preços":^30}")
print("-"*50)
for item in range(0, len(msg), 2):
    print(f"{msg[item]:.<30}", end="R$")
    print(f"{msg[item+1]:>5}")
print("-"*50)