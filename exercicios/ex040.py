n1 = int(input('Insira a primeira nota do aluno '))
n2 = int(input('Insira a segunda nota do aluno '))
m = (n1+n2)/2
print('A média dele é', m)
if m >= 6:
    print("Aprovado")
else:
    print("Reprovado")