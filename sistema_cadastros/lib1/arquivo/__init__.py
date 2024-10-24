from sistema_cadastros.lib1.interface import *

def arquivoExiste(nome): #funcao para verificar se o arquivo que armazenará os cadastros existe
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome): #funcao para criar o arquivo .txt caso ele nao exista 
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro ao criar o arquivo txt")
    else:
        print(f"Arquivo {nome} criado com sucesso")


       
def cadastrar(arq, nome, nserie, valor):
    try:
        a = open(arq, 'at')
    except:
        print("Erro na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{nserie};{valor}\n")
        except:
            print("Houve um erro ao gravar os dados!")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
        finally:
            a.close()


#def consultarProduto():


#def editarProduto():


def apagarProduto(arq,nome):
    a = nome
    linha_a_apagar = None

    try:
        with open(arq, "r") as file:
            linhas = file.readlines()
    except Exception as exc:
        print(f"Houve um erro na abertura do arquivo {exc}")
        return
    for numerolinha, linha in enumerate (linhas):
        if a in linha:
            linha_a_apagar = numerolinha

        
    if linha_a_apagar is not None:
        try:
            with open(arq,"w") as file:
                for numero, linha in enumerate(linhas):
                    if numero != linha_a_apagar:
                        file.write(linha)
            print(f"O produto {nome} foi removido com sucesso!")
        except Exception as exc:
            print(f"Houve um erro ao tentar reescrever o arquivo: {exc}")
    else:
        print(f"O produto '{nome}' não foi encontrado na lista.")

def exibirProdutos(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PRODUTOS CADASTRADOS")
        indice("Produto", " Serie", "  Valor\n")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            valor_formatado = f"{float(dado[2]):.2f}".replace('.', ',') #convertendo o valor para float para formatar com 2 casas decimais.
            print(f"{dado[0]:<20} {dado[1].center(10)} R${valor_formatado:>8}")
    finally:
        a.close()
