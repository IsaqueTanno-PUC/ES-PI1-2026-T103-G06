import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database="sistema_votacao",
            user="root",
            password="Fabri014*z"
        )
        if conexao.is_connected():
            # print ("Conexao com o banco realizada!") - Removi essa parte para não aparecer toda vez após a conexão ao banco
            return conexao
    except Exception as erro:
        print ("Nao foi possivel conectar ao banco. ERRO:", erro)
        return None, None