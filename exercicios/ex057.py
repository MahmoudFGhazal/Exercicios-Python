s = input("Informe seu sexo: [M/F] ").upper().strip()
while s not in "MF":
    s = print("Dados Invalidos, Insira Novamente: [M/F] ").upper().strip()
print("Sexo {} registrado com sucesso".format(s))
