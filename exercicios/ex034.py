n = float(input('Qual é o seu salario? '))
if n > 1250:
    print('R${:.2f}'.format(n*1.1))
else:
    print('R${:.2f}'.format(n*1.15))
