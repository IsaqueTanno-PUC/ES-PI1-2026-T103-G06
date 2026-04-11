import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database="sistema_votacao",
            user="root",
            password="Fabri014*"
        )
        if conexao.is_connected():
            print ("Conexao com o banco realizada!")
            cursor = conexao.cursor()
            return conexao, cursor
    except Exception as erro:
        print ("Nao foi possivel conectar ao banco. ERRO:", erro)
        return None, None