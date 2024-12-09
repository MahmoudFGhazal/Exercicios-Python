from exercicios.ex115.uteis.arquivo import *
from exercicios.ex115.uteis.dados import *

arq = "cadastro.txt"
arquivoExiste(arq)

while True:
    n = menu("Menu Principal", "Ver pessoas", "Cadastrar nova pessoa", escolha=True)
    match n:
        case 1:
            lerArquivo(arq)
        case 2:
            menu("Novo Cadastro")
            nome = input("Nome: ").strip().title()
            i = leiaInt("Idade: ")
            cadastrar(arq, nome, i)
        case 3:
            break
menu("Saindo do Sistema... Até Logo!")
