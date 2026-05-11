import random
import string
from datetime import datetime
from conexaoBD import conectar
from auditoria import registro_log, protocolo_votacao

def registrar_voto(eleitor_id, cand_numero):
    
    """
    Registra o voto no banco de dados.
    Args:
        eleitor_id (int): Id do eleitor que está votando.
        cand_numero (int): Número do candidato escolhido.
    Returns:
        str: Protocolo gerado.
    """
    conexao= conectar()
    cursor= conexao.cursor()

    horario= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    protocolo= "V" + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + "26" + str(cand_numero).zfill(2) + str(random.randint(10000, 99999))

    try:
        sql= "INSERT INTO votos (voto_horario, voto_candnumero, voto_protocolo) VALUES (%s, %s, %s)"
        valores= (horario, cand_numero, protocolo)
        cursor.execute(sql, valores)

        sql= "UPDATE eleitores SET eleitor_situacao= 1, eleitor_horavoto= %s WHERE eleitor_id= %s"
        valores= (horario, eleitor_id)
        cursor.execute(sql, valores)

        conexao.commit()
        registro_log("SUCESSO: Voto realizado com sucesso")
        protocolo_votacao(eleitor_id, cand_numero)
        print("Voto registrado com sucesso")
        print("Protocolo: ", protocolo)

    except Exception as erro:
        print("Erro ao registrar voto: ", erro)

    finally:
        cursor.close()
        conexao.close()