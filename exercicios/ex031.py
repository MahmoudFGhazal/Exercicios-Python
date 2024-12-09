d = float(input('Qual é a distancia da viagem(em km): '))
if d > 200:
    print('R${}'.format(d*0.45))
else:
    print('R${}'.format(d*0.5))
