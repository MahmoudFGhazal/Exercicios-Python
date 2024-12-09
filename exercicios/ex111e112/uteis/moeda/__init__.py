def resumo(p, a=10, r=5):
    traços("-")
    print(f"{"Resumo do Valor":^30}")
    traços("-")
    print(f"Preço Analisado: {moeda(p)}")
    print(f"Dobro do Preço: {dobro(p, True)}")
    print(f"Metade do Preço: {metade(p, True)}")
    print(f"{a}% de aumento: {porcentagem(p, a, format=True)}")
    print(f"{r}% de redução: {porcentagem(p, r, True, True)}")
    traços("-")


def traços(t):
    print(t*30)


def metade(num, format=False):
    num /= 2
    return num if not format else moeda(num)


def dobro(num, format=False):
    num *= 2
    return num if not format else moeda(num)


def porcentagem(num, a, d=False, format=False):
    if d:
        a *= -1
    a = a/100 + 1
    num *= a
    return num if not format else moeda(num)


def moeda(num):
    num = "R$" + f"{float(num):.2f}"
    num = num.replace(".", ",")
    return num
