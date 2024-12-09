def leiaInt(msg):
    while True:
        p = input(msg).strip()
        if p.isnumeric():
            return int(p)
        else:
            print("ERRO! Digite um número valido")


print("-"*30)
n = leiaInt("Digite um número: ")
print(n)
