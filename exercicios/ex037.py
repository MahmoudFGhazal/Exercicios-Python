n = int(input("Insira um número inteiro: "))
print("Escolha uma das opções:")
print("1. converter para binario")
print("2. converter para octal")
print("3. converter para hexadecimal")
escolha = input("Sua opção: ")
escolha = escolha.strip()

if escolha == "1":
    print("{} em binario é {}".format(n, bin(n)[2:]))
elif escolha == "2":
    print("{} em octal é {}".format(n, oct(n)[2:]))
elif escolha == "3":
    print("{} em hexadecimal é {}".format(n, hex(n)[2:]))
else:
    print("Opção Invalida")
