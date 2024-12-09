numeros = ("zero", "um", "dois", "tres", "quatro", "cinco",
           "seis", "sete", "oito", "nove", "dez")
while True:
    n = int(input("Digite um número de 0 a 10: "))
    if 0 <= n <= 10:
        break
    print("Tente Novamente. ", end="")
print(f"Você digitou o número {numeros[n]}")
