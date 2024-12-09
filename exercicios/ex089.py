p = []
while True:

    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/ 2
    p.append([nome, [nota1, nota2], media])
    if input("Você quer continuar? ").strip() in "nN":
        break
print("-="*30)
print(f"{"No.":<4}{"Nome":<10}{"Media":>8}")
print("-"*30)
for cont, c in enumerate(p):
    print(f"{cont+1}   {c[0]}" + " "*10 + str(c[2]))
while True:
    print("-"*30)
    n = int(input("Mostrar a nota de qual aluno? (0 Interrompe) "))
    if n == 0:
        break
    notas = p[n-1]
    print(f"Notas de {notas[0]} são {notas[1]}")
