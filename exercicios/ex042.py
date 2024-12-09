a = int(input('Insira o primeiro lado do triangulo: '))
b = int(input('Insira o segundo lado do triangulo: '))
c = int(input('Insira o terceiro lado do triangulo: '))
if a + b > c and b + c > a and a + c > b:
    print('Triangulo possivel')
    if a == b == c:
        print("Equilatero")
    elif a != b != c != a:
        print("Escaleno")
    else:
        print("Isosceles")
else:
    print('Triangulo impossivel')