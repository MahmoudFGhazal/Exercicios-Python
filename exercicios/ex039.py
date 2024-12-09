a = int(input("Ano de nascimento: "))
print("nasceu em {} tem {} anos em 2024".format(a, 2024-a))
if 2024 - a < 18:
    print("Ainda falta {} anos para o alistamento".format(18-2024+a))
    print("Seu alistamento será em {}".format(a+18))
elif 2024 - a >= 18:
    print("Você se alistou à {} anos".format(-18 + 2024 - a))
    print("Seu alistamento foi em {}".format(a + 18))
