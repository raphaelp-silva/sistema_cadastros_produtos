import mysql.connector
from sistema_cadastros.lib1.interface import *
import pandas as pd

conexao = mysql.connector.connect(
        host="localhost",  # ou o endereço IP do servidor MySQL
        user="root",
        password="raphael95",
        database="sistema_cadastros"
    )

cursor = conexao.cursor()

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


def apagarProduto(nome):
    try:
        cursor.execute("SELECT COUNT(*) FROM produtos WHERE nome_produto = %s;", (nome,))
        existe = cursor.fetchone()[0]

        if existe == 0:
            print(f"Produto '{nome}' não encontrado!")
            return False
        
        cursor.execute("DELETE FROM produtos WHERE nome_produto = %s;", (nome,))
   
        conexao.commit()

        print(f"Produto '{nome}' excluído com sucesso!")
        return True
    except Exception as exc:
        print(f"Houve um erro na exclusão do produto: {exc}")
        return False


def exibirProdutos():
    try:
        cursor.execute("SELECT * FROM produtos;")
        resultado = cursor.fetchall()
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
    else:
        cabecalho("PRODUTOS CADASTRADOS")
        # Verifica se há produtos cadastrados
        if resultado:
            df = pd.DataFrame(resultado, columns=["Nome", "Série", "Preço"])
            print(df.to_string(justify="center"))
        else:
            print("Nenhum produto cadastrado.")
