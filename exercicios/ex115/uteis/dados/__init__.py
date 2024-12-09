def menu(* op, escolha=False):
    msg = "-"*50
    msg += f"\n{op[0]:^50}\n"
    msg += "-"*50
    if escolha:
        return interativo(op[1:], msg)
    print(msg)


def interativo(op, msg):
    for c, i in enumerate(op):
        msg += f"\n{c+1} - {i}"
    msg += f"\n{len(op)+1} - Sair do Sistema\n"
    msg += "-"*50
    print(msg)
    while True:
        try:
            e = int(input("Sua Opção: "))
        except ValueError:
            print("Valor Incorreto")
        except KeyboardInterrupt:
            print("Programa Interrompido")
            quit()
        else:
            if 0 < e < 4:
                return e
            print("Esse Valor não é uma opção")
            print(msg)


def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return int(n)
        print("Idade Invalida")