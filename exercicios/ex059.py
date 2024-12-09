o = 0
v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
while o != 5:
    print("------ Menu -----")
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Maior")
    print("4. Novos Números")
    print("5. Sair do Programa")
    o = int(input("Qual é a sua opção? "))
    if o == 1:
        print("{} + {} = {}".format(v1, v2, v1+v2))
    elif o == 2:
        print("{} x {} = {}".format(v1, v2, v1*v2))
    elif o == 3:
        print("Entre {} e {}, o maior é {}".format(v1, v2,v1 if v1 > v2 else v2))
    elif o == 4:
        print("Informe os números novamente")
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))
    elif o == 5:
        print("Finalizando...")
    else:
        print("Opção Invalida")