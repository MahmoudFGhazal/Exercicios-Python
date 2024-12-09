while True:
    n = input("Quer ver a tabuada de números positivo de qual valor? [sair] ")
    if not n.isnumeric():
        n.lower().strip()
        if n == 'sair':
            print("-" * 30)
            break
        else:
            print("Opção Invalida")
            continue
    n = int(n)
    for c in range(1, 11):
        print(f"{n} x {c} = {c*n}")
    print("-" * 30)
print("Programa Finalizado")
