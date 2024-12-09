while True:
    try:
        n = int(input("Digite um Inteiro: "))
    except ValueError:
        print("Valor Invalido, insira um número inteiro")
    except KeyboardInterrupt:
        print("O programa foi Interropido")
        quit()
    else:
        break
while True:
    try:
        p = float(input("Digite um Real: "))
    except ValueError:
        print("Valor Invalido, insira um número real")
    except KeyboardInterrupt:
        print("O programa foi Interropido")
        quit()
    else:
        break
print(f"O valor inteiro digitado foi {n} e o real foi {p}")
