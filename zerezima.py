import conexaoBD
from conexaoBD import conectar
import auditoria
from auditoria import registro_log

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
        cursor.execute("TRUNCATE TABLE votos;")
        cursor.execute("UPDATE eleitores SET eleitor_situacao=0 WHERE eleitor_situacao=1;")
        conexao.commit()
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
        bool: False, caso não haja candidatos; True, quando houver candidatos & Exibição dos candidatos e seus votos no terminal
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
            registro_log("Votação não realizada, nenhum candidato cadastrado!")
            print("NENHUM CANDIDATO CADASTRADO")
            return False

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
            return True
            
    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()