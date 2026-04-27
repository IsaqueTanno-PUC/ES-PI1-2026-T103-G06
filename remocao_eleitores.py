from conexaoBD import conectar
 
def remover_eleitor():
    """
    Realiza a busca de um eleitor pelo CPF ou título e o remove do banco de dados
 
    Args:
        Input do usuário dentro da função
 
    Returns:
        Em caso positivo, remove o eleitor do banco de dados e exibe uma mensagem de confirmação
 
    """
 
    conexao = None
    cursor = None
 
    try:
        conexao = conectar()
        cursor = conexao.cursor()
 
        print("\n\n=====Remover Eleitor=====\n")
 
        # pergunta como o usuário quer buscar o eleitor
        print("Deseja encontrar o eleitor por:")
        print("[1] CPF")
        print("[2] Título de eleitor")
        print("[3] Cancelar")
 
        escolha = ""
        while escolha not in ["1", "2", "3"]:
            escolha = input("Digite sua opção: ")
            if escolha not in ["1", "2", "3"]:
                print("Opção inválida! Digite 1, 2 ou 3")
 
        if escolha == "1":
            cpf = input("Digite o CPF do eleitor: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            sql = "SELECT * FROM eleitores WHERE eleitor_cpf = %s"
            cursor.execute(sql, (cpf,))
 
        elif escolha == "2":
            titulo = input("Digite o título de eleitor: ")
            titulo = titulo.replace(".", "")
            titulo = titulo.replace("-", "")
            sql = "SELECT * FROM eleitores WHERE eleitor_titulo = %s"
            cursor.execute(sql, (titulo,))
 
        else:
            print("Operação cancelada.")
            return
 
        # pega o resultado da busca
        resultado = cursor.fetchone()
 
        # se não encontrou ninguém
        if resultado == None:
            print("Eleitor não encontrado.")
            return
 
        # mostra os dados do eleitor encontrado
        print("\nEleitor encontrado:")
        print("Nome: " + resultado[1])
        print("Título: " + resultado[2])
        print("CPF: " + resultado[3])
 
        # salva o id e o nome para usar depois
        eleitor_id = resultado[0]
        eleitor_nome = resultado[1]
 
        # pede confirmação antes de apagar
        print("\nTem certeza que deseja remover " + eleitor_nome + "?")
        print("1 - Sim")
        print("2 - Não")
 
        confirmacao = ""
        while confirmacao not in ["1", "2"]:
            confirmacao = input("Digite sua opção: ")
            if confirmacao not in ["1", "2"]:
                print("Opção inválida! Digite 1 ou 2")
 
        if confirmacao == "1":
            sql_delete = "DELETE FROM eleitores WHERE eleitor_id = %s"
            cursor.execute(sql_delete, (eleitor_id,))
            conexao.commit()
            print("Eleitor removido com sucesso!")
 
        else:
            print("Remoção cancelada.")
 
    except Exception as erro:
        print("Erro: ", erro)
 
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
