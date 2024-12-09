a = int(input("Ano de nascimento: "))
idade = 2024 - a
print("nasceu em {} tem {} anos em 2024".format(a, idade))
if idade < 9:
    print("Mirim")
elif idade < 14:
    print("Infantil")
elif idade < 19:
    print("Junior")
elif idade < 25:
    print("Senior")
else:
    print("Master")
