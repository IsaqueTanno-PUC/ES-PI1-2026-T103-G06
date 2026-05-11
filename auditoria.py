from datetime import datetime

def registro_log(mensagem):
    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ("logs_ocorrencias.txt", "a", encoding="UTF-8") as arquivo:
        arquivo.write(f"{hora} - {mensagem}\n")


def protocolo_votacao(protocolo):
    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open ("protocolo_votacao.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{hora} - Protocolo: {protocolo}\n")