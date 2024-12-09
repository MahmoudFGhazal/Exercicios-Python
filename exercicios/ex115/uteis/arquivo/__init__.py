from exercicios.ex115.uteis.dados import menu


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        print("Arquivo Não Encontrado")
        criarArquivo(nome)


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except Exception as error:
        print(f"Houve um Erro na criação do arquivo\n{error.__class__}")
        quit()
    else:
        print("Arquivo Criado")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except Exception as error:
        print(f"Houve um Erro para abrir o arquivo\n{error.__class__}")
    else:
        menu("Pessoas Cadastradas")
        for c in a:
            dado = c.split(":")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, "at")
    except Exception as error:
        print(f"Houve um erro na abertura do arquivo\n{error.__class__}")
    else:
        try:
            a.write(f"{nome}:{idade}\n")
        except Exception as error:
            print(f"Houve um erro na hora de alterar o arquivo\n{error.__class__}")
        else:
            print(f"Novo registro de {nome} adicionado.")
    finally:
        a.close()
