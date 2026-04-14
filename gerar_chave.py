import random
import conexaoBD
from conexaoBD import conectar

def eleitor_chave_de_acesso(nome1,nome2):
    """
        Cria a chave de acesso única, com base no nome fornecido pelo usuário

    Args:
        nome1(string): O primeiro nome do usuário
        nome2(string): O segundo nome do usuário

    Returns:
        string: chave única gerada
    """

    conexao = conectar()
    cursor = conexao.cursor()
    chave=""
    chavebase=(""+nome1[0]+nome1[1]+nome2[0]).upper()
    valido=0
    while(valido==0):
        chave=chavebase
        cont=0
        while(cont<4):
            n=random.randint(0,9)
            chave=chave+str(n)
            cont=cont+1
        
        cursor.execute("SELECT eleitor_chaveacesso FROM eleitores WHERE eleitor_chaveacesso = %s", (chave,))
        copia=cursor.fetchone()
        if not copia:
            valido=1
            cursor.close()
            conexao.close()
            return chave
    