import mysql.connector
from sistema_cadastros.lib1.interface import *
import pandas as pd

conexao = mysql.connector.connect(
        host="localhost",  
        user="root",
        password="raphael95",
        database="sistema_cadastros"
    )

cursor = conexao.cursor()

def cadastrar(nome, nserie, valor):
    try:
        cursor.execute(f"INSERT INTO produtos (nome_produto, num_serie, valor) VALUES ('{nome}', '{nserie}', {valor})")
        conexao.commit()
        print(f"O produto '{nome}' foi cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar o produto: ", e)

def consultarProduto(nome):
    try:
        cursor.execute(f"SELECT * FROM produtos WHERE nome_produto = '{nome}'")
        resultado = cursor.fetchall()
    except Exception as e:
        print("Erro ao consultar o produto:", e)
    else:
        cabecalho("PRODUTOS ENCONTRADOS")
        if resultado:
            df = pd.DataFrame(resultado, columns=["Nome", "Série", "Preço"])
            print(df.to_string(justify="center"))
        else:
            print("Nenhum produto encontrado.")


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
