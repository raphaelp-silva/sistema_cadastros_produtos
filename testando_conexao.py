import mysql.connector
from mysql.connector import Error

try:
    # Conecte-se ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",  # ou o endereço IP do servidor MySQL
        user="root",
        password="raphael95",
        database="sistema_cadastros"
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")
        
        # Executa uma consulta de teste para verificar a conexão
        cursor = conexao.cursor()
        cursor.execute("SELECT DATABASE();")
        banco = cursor.fetchone()
        print("Banco de dados atual:", banco[0])

except Error as e:
    print("Erro ao conectar ao MySQL:", e)

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão ao MySQL encerrada.")
