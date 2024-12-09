n = int(input('Insira um número '))
print('='*10, '\n' + str(n), '{:^4}'.format('* 1 ='), n)
print(n, '{:^4}'.format('* 2 ='), n*2)
print(n, '{:^4}'.format('* 3 ='), n*3)
print(n, '{:^4}'.format('* 4 ='), n*4)
print(n, '{:^4}'.format('* 5 ='), str(n*5) + '\n' + '='*10)

