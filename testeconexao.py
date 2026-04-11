from conexaoBD import conectar

conexao, cursor = conectar()

if conexao:
    print("conectado com sucesso!")
else:
    print("nao foi possivel conectar ao banco.")