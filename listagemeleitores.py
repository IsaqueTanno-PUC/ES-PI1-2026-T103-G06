import mysql.connector
from conexaoBD import conectar

def listar_eleitores():
    """
    Lista todos os eleitores cadastrados no banco de dados.
    Args:
        Nenhum.
    Returns:
        None: Apenas exibe os eleitores no terminal.
    """
    try:
        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute("SELECT eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario FROM eleitores ORDER BY eleitor_nome")
        eleitores=cursor.fetchall()
        if len(eleitores)==0:
            print("NENHUM ELEITOR CADASTRADO")
        else:
            print("\nLISTA DE ELEITORES\n")
            cont=0
            while cont<len(eleitores):
                nome,titulo,cpf,mesario=eleitores[cont]
                if mesario == 1:
                    status_mesario="SIM"
                else:
                    status_mesario="NÃO"
                print("Nome: ", nome)
                print("Título: ", titulo)
                print("CPF: ", cpf)
                print("Mesário: ", status_mesario,"\n")
                cont=cont+1
            print("TOTAL ELEITORES: ", len(eleitores))
    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()