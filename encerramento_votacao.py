import conexaoBD
from conexaoBD import conectar
 
def encerrar_votacao():
    """
    Solicita as informações do mesário e encerra o sistema de votação
    Args:
        Nenhum
    Returns:
        bool: True se o encerramento for bem sucedido e False se houver algum cancelamento, erro, ou eleitor não é mesário
    """
    try:
        conexao = conectar()
        cursor = conexao.cursor()
 
        print("\n=====Encerramento da Votação=====\n")
        print("Digite CANCELAR caso deseje sair deste processo")
 
        # validação do título
        titulo = "a"
        while len(titulo) != 12 or titulo.isdigit() == False:
            try:
                titulo = input("Digite o título de eleitor: ").strip()
                if titulo.upper() == "CANCELAR":
                    print("Processo cancelado...")
                    return False
                elif len(titulo) != 12 or titulo.isdigit() == False:
                    print("\nErro! Digite um título válido!")
            except:
                titulo = "a"
                print("\nErro! Digite um título válido!")
 
        # validação dos 4 primeiros dígitos do CPF
        cpf = "a"
        while len(cpf) != 4 or cpf.isdigit() == False:
            try:
                cpf = input("Digite os 4 primeiros dígitos do CPF: ").replace(".", "").strip()
                if cpf.upper() == "CANCELAR":
                    print("Processo cancelado...")
                    return False
                elif len(cpf) != 4 or cpf.isdigit() == False:
                    print("\nErro! Digite 4 dígitos válidos!")
            except:
                cpf = "a"
                print("\nErro! Digite 4 dígitos válidos!")
 
        # validação da chave de acesso
        chave = "a"
        while len(chave) != 7:
            try:
                chave = input("Digite a chave de acesso: ").strip()
                if chave.upper() == "CANCELAR":
                    print("Processo cancelado...")
                    return False
                elif len(chave) != 7:
                    print("\nErro! Digite uma chave de acesso válida!")
            except:
                chave = "a"
                print("\nErro! Digite uma chave de acesso válida!")
 
        # busca o eleitor no banco verificando título, CPF e chave de acesso
        # a verificação com criptografia (Cifra de Hill) será implementada futuramente
        sql = "SELECT eleitor_titulo, eleitor_cpf, eleitor_chaveacesso, eleitor_mesario FROM eleitores WHERE eleitor_titulo = %s AND eleitor_cpf LIKE %s AND eleitor_chaveacesso = %s"
        cpf = cpf + "%"
        aux = (titulo, cpf, chave)
 
        cursor.execute(sql, aux)
        resultado = cursor.fetchone()
 
        if resultado == None:
            print("Não foi possível encerrar! Usuário não encontrado!")
            return False
 
        elif resultado[3] == 0:
            print("Não foi possível encerrar! Eleitor não é mesário!")
            return False
 
        # pede confirmação antes de encerrar
        print("\nDeseja realmente encerrar a votação?")
        print("1 - Sim")
        print("2 - Não")
 
        confirmacao = ""
        while confirmacao not in ["1", "2"]:
            confirmacao = input("Digite sua opção: ")
            if confirmacao not in ["1", "2"]:
                print("Opção inválida! Digite 1 ou 2")
 
        if confirmacao == "2":
            print("Encerramento cancelado.")
            return False
 
        # segunda confirmação com a chave de acesso
        chave2 = "a"
        while len(chave2) != 7:
            try:
                chave2 = input("\nDigite sua chave de acesso novamente para confirmar: ").strip()
                if chave2.upper() == "CANCELAR":
                    print("Processo cancelado...")
                    return False
                elif len(chave2) != 7:
                    print("\nErro! Digite uma chave de acesso válida!")
            except:
                chave2 = "a"
                print("\nErro! Digite uma chave de acesso válida!")
 
        if chave2 != resultado[2]:
            print("Erro: chave de acesso incorreta!")
            return False
 
        # encerramento confirmado
        print("\nVotação encerrada com sucesso!")
        return True
 
    except Exception as erro:
        print("Erro inesperado: ", erro)
        return False
 
    finally:
        cursor.close()
        conexao.close()
