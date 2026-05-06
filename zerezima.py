import conexaoBD
from conexaoBD import conectar

def zerar_votos():
    """
    Apaga todos os registros de votos do banco de dados
    Args:
        Nenhum
    Returns:
        Faz a limpeza da tabela 'votos' do banco de dados
    """
    try:
        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute("TRUNCATE TABLE votos")
    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()

def listar_candidatos():
    """
    Lista todos os candidatos cadastrados no banco de dados
    Args:
        Nenhum
    Returns:
        Exibição dos candidatos e seus votos no terminal
    """
    try:
        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute("""  SELECT 
                                can_nome,
                                cand_numero,
                                cand_partido,
                                (
                                    SELECT COUNT(*)
                                    FROM votos
                                    WHERE votos.voto_candnumero = candidatos.cand_numero
                                ) AS total_votos
                            FROM candidatos
                            ORDER BY can_nome;""")
        candidatos=cursor.fetchall()

        if len(candidatos)==0:
            print("NENHUM CANDIDATO CADASTRADO")

        else:
            print("LISTA DE CANDIDATOS")
            cont=0
            while cont<len(candidatos):
                nome,numero,partido,votos=candidatos[cont]
                print(f"\nNome: {nome}")
                print(f"Número: {numero}")
                print(f"Partido: {partido}")
                print(f"Votos: {votos}")
                cont=cont+1

            print("\nTOTAL CANDIDATOS: ", len(candidatos))
            
    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()