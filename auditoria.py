import conexaoBD
from conexaoBD import conectar
from datetime import datetime

def registro_log(mensagem):
    conexao=conectar()
    cursor=conexao.cursor()
    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ("logs_ocorrencias.txt", "a", encoding="UTF-8") as arquivo:
        arquivo.write(f"{hora} - {mensagem}\n")


def protocoto_votacao(eleitor_id, candidato):
    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ("protocoto_votacao.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"ID do Eleitor: {eleitor_id}\n")
        arquivo.write(f"Candidato: {cand_nome}\n")
        arquivo.write(f"Data e Hora: {hora}\n")
        arquivo.write("Voto computado")