import conexaoBD
from conexaoBD import conectar
from validar import cpf

def cadastrar_eleitor():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CADASTRO DE ELEITOR ===")
        eleitor_nome = input ("Digite seu nome: ")
        eleitor_titulo = input ("Digite seu titulo de eleitor: ")
        #essa parte depois do input de cpf "remove" os acentos do CPF (caso tiver) e deixa sem pontuacao para evitar parar o programa
        eleitor_cpf = input ("Digite seu CPF: ").replace(".", "").replace("-", "")
        if cpf(eleitor_cpf):
            print ("CPF inválido!")
            return
        eleitor_mesario = input ("Sera mesario?\n(0)NAO\n(1)SIM\n")

        sql = """
        INSERT INTO eleitores (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario)
        VALUES (%s, %s, %s, %s)"""

        valores = (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Eleitor cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar eleitor:", erro)

    finally:
        cursor.close()
        conexao.close()
