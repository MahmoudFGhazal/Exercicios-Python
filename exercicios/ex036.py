c = float(input("Qual é o valor da casa? "))
s = float(input("Qual é o salario? "))
a = int(input("Em quantos prestações você vai pagar? "))
if c / a > 0.3 * s:
    print("Emprestimo recusado")
else:
    print("Emprestimo aprovado")
