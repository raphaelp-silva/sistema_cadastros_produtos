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
        cursor.execute("USE sistema_cadastros;")
        #revisar pq nao entra no banco 
        cursor.execute("INSERT INTO produtos values ('teste','teste123','200')")

except Error as e:
    print("Erro ao conectar ao MySQL:", e)

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão ao MySQL encerrada.")
