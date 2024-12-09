from datetime import datetime


def voto(n):
    n = datetime.now().year - n
    if n >= 18:
        print(f"Com {n} anos: Voto Obrigatorio")
    elif n >= 16:
        print(f"Com {n} anos: Voto Opcional")
    else:
        print(f"Com {n} anos: Não Vota")


print("-"*30)
n = int(input("Em que ano você nasceu? "))
voto(n)
