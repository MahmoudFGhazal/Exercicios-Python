# Comandos

# int = inteiro
# float =  numeros com virgula
# bool = boolean, outro caso se tiver alguma coisa guardado é verdadeiro se não é falso
# str = String
# print
# input
# if
# elif
# else
# if vendas:=(int(input("Quantidade de vendas"))) < 100: == salva o input
# and
# or
# in = se estiver dentro
# while
# break
# continue
# import "Exemplo" = importa todo exemplo
# from "Exemplo" import = importa um objeto
# for "variavel" in range(inicio, fim, passo):
# while not "": ou while "":
# while True: e break
# Exemplo[2] == vai mostrar a terceira coisa guardadana variavel composta
# Exemplo[0:2] == vai mostrar da primeira a terceira coisa quardada na variavel
# Exemplo[1:] == vai mostrar da segunda a ultima coisa quardada na variavel
# Exemplo[-1] == vai mostrar a ultima coisa quardada na variavel
# len(Exemplo) == pega o tamanho de Exemplo
# for "variavel" in Exemplo: == vai usar a variavel composta para mudar a "variavel"
# Obs: variveis compostas são inmutaveis
# sorted(Exemplo) == coloca em ordem alfabetica ou do maior para menor
# map(oque você quer fazer, variavel composta) == mapea cada variavel de uma variavel composta utilizando a função
# try except else finally == try e o excepet são tente se não faça, e o else significa se deu certo faça, finally sempre vai fazer, mesmo se der errado
# except Exception as erro: == está dizendo que erro é a exceção
# erro.__class__ == é usado para ver qual tipo de erro
# Obs: um try pode ter mais de um exception
# quit() ou exit() finaliza o programa

# Listas

# dados = list() or dados = [] == cria uma lista
# Exemplo.append() = adiciona um valor a uma lista
# Exemplo.insert("Lugar", "variavel") == inseri a variavel no local onde você pediu, empurando o resto para direita
# del Exemplo[local]
# Exemplo.pop() == remove o ultimo elemento da lista
# Exemplo.remove("Nome da variavel") == nesse caso você pede para retirar a variavel não o local em especifico
# Exemplo.index("oque você quer procurar") == ele procura dentro de uma variavel composta ou uma lista e conta quantas vezes se repete
# Exemplo1 = list(range(4,11)), cria uma lista de números com esse range
# Exemplo.sort() == Ordena os valores numericos em ordem
# Exemplo.sort(reverse=True) == Ordena em ordem decrecente
# Exemplo.append(Exemplo[:]) == inseri uma lista dentro de uma lista, ou seja, ficaria assim Exemplo = [["Variavel1", "Variavel2"], ["variavel3", "Variavel4"]]
# print(Exemplo[0][0])
# matriz = [[0] * 3 for _ in range(3)]
# dicionarios == {} == são lista separadas, ao invez numeros, por nomes
# Exemplo = {"nome": "Pedro", "idade":25} e se print(Exemplo["nome"] == "Pedro"
# Exemplo["sexo"] = "M"
# del Exemplo["sexo"]
# print(Exemplo.values()) == ["Pedro", 25]
# print(Exemplo.keys()) == ["nome", "idade"]
# print(Exemplo.items()) == ["nome": "Pedro", "idade":25]
# Exemplo.append(Dicionario.copy())
# match / case / case _ / case "variavel" if "codição"
# sorted == ordena as listas
# sum() == soma de número de uma lista
# max() == pega o maior
# min() == pega o menor
# | == fusão entre dicionarios
# batched() == separa lista em grupos, batched(Exemplo, 2) == vai serpara o exemplo em varias lista com 2 elemento cada


# Funções e Modulos

# def Exemplo: == Função
# def Exemplo(* exemplo): == se você não saber quantos variaveis vai receber e transformar em uma tupla
# def Exemplo(list) == transforma em uma lista
# para passar parametros, podemos fazer o seguinte:
# def função(a=0, b=0, c=0): == a gente pode passar "função(b=2, c=4) e o "a = 0"
# as variaveis criadas no main pode ser usada em qualquer lugar enquanto as criadas dentro da função não podem ser usadas em outros lugares
# se eu quiser mudar a variavel global dentro de uma função preciso usar:
# global Exemplo
# import "nome do arquivo", ai você tem que colocar """nome do arquivo"."nome da função"()""

# NUMEROS

# ** = potencia = pow(x,y)
# // = divisão inteira
# % = resto da divisão
# bin(Exemplo) = binario
# oct(Exemplo) = Octal
# hex(Exemplo) = Hexdecimal

# Bibliotecas: math, random, time, operator, urllib, tempfile, itertools

# STRINGS

# type() = faz com que mostre o tipo de variavel
# .isnumeric() = é usado para ver se todos os carcters de um string são numeros
# .isalpha() = é usado para ver se todos os carcters de um string são letras
# .isalnum() => isnumeric() ou isalpha()
# .isupper() = se todas as letras são maisculas
# .islower() = se todas as letras são minusculas
# .isdecimal() = se todas as letras são decimais
# .isprintavle() = se todas as eltras são primiveis (não tenha \n, por exemplo)
# .isspace() = se tem espaço
# .istitle() = se todas as letras começam com maisculas
# "m" * 5 == "mmmmm"
# print('oi {:2}').format('5') == sempre vai deixar os espaços para isso
# print('oi {:>20}').format('5') == 'oi (20 espaços) 5'
# print('oi {:<20}').format('5') == 'oi 5 (20 espaços)'
# print('oi {:^20}').format('5') == 'oi (10 espaços) 5 (10 espaços)'
# print('oi {:'Exemplo'20}').format('5') == 'oi (10 'Exemplo') 5 (10 'Exemplo')'
# print('oi {:.3f}').format(5.55555) == só vai deixar 3 casas decimais
# print("I'm", end = "Pode ser qualquer coisa")
# print("gay") == os dois vão ficar na mesma linha
# \n = nova linha
# frase = "I'm gay", se você pedir frase[3] == "m" ou se frase[3:6] == "m g" ou se frase[3:6:2] == "mg" ou se frase[:6] = "I'm g" ou se frase[3:] == "m gay"
# len(Exemplo) = ve o tamanho de uma string
# Exemplo.count('letra') = conta quantos letras vai ter dentro de uma string
# Exemplo.count('letra', 0, 6) =  vamos pegar a "I'm gay" como exemplo, vai pegar uma letra da posição 0 até a 6
# Exemplo.find('deo') = quantas vezes tem dentro de uma string e vai dizer quando começou
# 'palavra' in Exemplo = ele vai retornar verdadeiro ou falso se tem a palavra dentro da string
# Exemplo.replace('palavra', 'outra palvra') = troca a 'palavra' pela a 'outra palavra'
# Exemplo.upper() = deixa a string toda em maisculo
# Exemplo.lower() = deixa a string toda em minusculo
# Exemplo.capitalize() = deixa somente a primeira letra da string maisculo
# Exemplo.title() = deixa todas os inicios de palavras em maisculo
# Exemplo.strip() = remove todos os espaços inuteis, exemplo, "   maoi é foda  ", vao ficar "maoi é foda'
# Exemplo.rstrip() = remove todos os espaços inuteis na direita, exemplo, "   maoi é foda  ", vao ficar "   maoi é foda'
# Exemplo.lstrip() = remove todos os espaços inuteis na esquerda, exemplo, "   maoi é foda  ", vao ficar "maoi é foda   '
# Exemplo.split() = divide as palavras considerando os espaços
# 'letra'.join(Exemplo) = junta as strings com a 'letra', exemplo, Exemplo tem 'oi' e 'tchau', se fizermos '-'.join(Exemplo'), ele vai ficar 'oi-tchau'
# print('carro novo' if tempo<=3 else 'carro velho')
# print(f"Frase {Exemplo}") == com o 'f' na frente você pode colocar a variavel direto nas chaves
# print("Frase %d" % "Exemplo") == jeito antigo, substitui, o d é porque é número

# Graficos

# Cor no texto: \033['Style; text; back'm
# Styles: 0 - Nenhum estilo, 1 - Negrito, 4 - Sublinhado, 7 - cores negativas
# text: 30 a 37
# back: 40 a 47
# Exemplo:  print('\033[1;31;43mOlá, Mundo!\033[m')
# Exemplo:  print('Olá, {}!'.format('\033[1;31;43mMundo'))

# Coleções
# Exemplo:
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m]'}
# print('Olá, {}!'.format(cores['azul'] + 'Mundo'))

# Ajuda

# pode ir para o phyton console e colocar help() e depois qualquer comando que ele vai dizer oq faz
# outro jeito você pode print(Exemplo.__doc__) ou help(Exemplo)
# docstring, você pode fazer um manual da sua função usando """ para escrever seu manual
