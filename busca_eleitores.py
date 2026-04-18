from conexaoBD import conectar

def busca_eleitor ():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print ("\n\n========Busca de eleitor========\n")
        escolha = input ("Deseja encontrar um eleitor por:\n[1]CPF\n[2]Titulo de eleitor\n ").replace(".", "").replace("-", "")
        if escolha == "1":
            cpf = input ("\nDigite o CPF do eleitor para busca: ")
            sql = "SELECT * FROM eleitores WHERE eleitor_cpf = %s"
            cursor.execute (sql, (cpf,))

        elif escolha == "2":
            titulo = input ("\nDigite o titulo do eleitor para busca: ").replace(".", "").replace("-", "")
            sql = "SELECT * FROM eleitores WHERE eleitor_titulo = %s"
            cursor.execute (sql, (titulo,))
        else:
            print ("Opcão invalida!")
            return

        resultado = cursor.fetchone()

        if resultado:
            print ("\nEleitor encontrado!\n")
            print (f"Nome: {resultado[1]}")
            print (f"Titulo de ELeitor: {resultado[2]}")
            print (f"CPF: {resultado[3]}")
        else:
            print ("Eleitor não encontrado na base de dados.")

    except Exception as erro:
        print ("Erro na busca: ", erro)

    finally:
        conexao.close()
        cursor.close()
