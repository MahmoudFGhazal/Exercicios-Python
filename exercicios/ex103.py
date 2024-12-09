def msg(nome, gols):
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


nome = input("Nome do jogador: ").strip()
gols = input("Numero de gols: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == "":
    nome = "<desconhecido>"

print(msg(nome, gols))
