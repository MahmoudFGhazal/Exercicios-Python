p = float(input("Qual é o peso? "))
a = float(input("Qual é a altura? "))
m = p / a ** 2
print("IMC = {:.1f}".format(m))
if m < 18.5:
    print("Abaixo do Peso")
elif m <= 25:
    print("Peso Ideal")
elif m <= 30:
    print("Sobrepeso")
elif m <= 40:
    print("Obesidade")
else:
    print("Obesidade Morbida")
