from conexaoBD import conectar
import os

conexao, cursor = conectar()

if conexao:
    print("conectado com sucesso")
else:
    print("nao foi possivel conectar")