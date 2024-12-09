def leiaMoeda(msg):
    while True:
        p = input(msg).strip()
        if p.isnumeric():
            p = float(p)
            return p
        print(f"ERRO: '{p}' é um preço inválido!")
