import conexaoBD
from conexaoBD import conectar
import validar
import validacao_titulo
import gerar_chave
import mysql.connector
import auditoria
from auditoria import registro_log

def cadastrar_eleitor():
    """
    Realiza a leitura dos dados do eleitor, passando pelas validações do título/cpf e exibe a chave de acesso única gerada
    
    Args:
        Input do usuário dentro da função

    Returns:
        Em caso positivo, realiza o cadastro no banco de dados e exibe a chave de acesso única
    
    """

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Fiz um ajuste para validar o nome (nome + sobrenome)
        print("\n=== CADASTRO DE ELEITOR ===")
        
        continuar_nome = 1

        while continuar_nome == 1:
            eleitor_nome = input("Digite seu nome: ")

            nome1 = ""
            nome2 = ""
            nome = str(eleitor_nome)
            nome_nchar = len(nome)
            cont = 0

            while cont < nome_nchar and nome[cont] != " ":
                nome1 = nome1 + nome[cont]
                cont = cont + 1

            cont = cont + 1

            while cont < nome_nchar and nome[cont] != " ":
                nome2 = nome2 + nome[cont]
                cont = cont + 1

            if nome1.isalpha() == False or nome2.isalpha() == False:
                registro_log("Usuario digitou apenas o primeiro nome ou caracteres que não são letras")
                print("Nome inválido! Digite apenas letras e coloque pelo menos o segundo nome.")

                conti_nome = int(input("Deseja continuar o cadastro?\n1 - Continuar\n2 - Voltar\n"))
                if conti_nome == 2:
                    return
            else:
                continuar_nome = 0


        #verificação e validação do titulo de eleitor do usuario:
        continuar_titulo = 1

        while continuar_titulo == 1:
         eleitor_titulo = input ("Digite seu titulo de eleitor: ").replace(".", "").replace("-", "")
         if validacao_titulo.validar_titulo(eleitor_titulo)==False:
             print ("Titulo de Eleitor inválido!")
             registro_log("tentativa de cadastro com titulo de Eleitor inválido")
             conti_titulo = int(input("Deseja continuar o cadastro?\n1 - Continuar\n2 - Voltar\n"))
             if conti_titulo == 2:
                 return
         else:
             continuar_titulo = 0




        #essa parte depois do input de cpf "remove" os acentos do CPF (caso tiver)
        #e deixa sem pontuacao para evitar parar o programa também faz a validação do CPF do usuario
        continuar_cpf = 1

        while continuar_cpf == 1:
         eleitor_cpf = input ("Digite seu CPF: ").replace(".", "").replace("-", "")
         if validar.cpf(eleitor_cpf)==False:
            registro_log("tentativa de cadastro com CPF invalido!")
            print ("CPF inválido!")
            conti_cpf = int(input("Deseja continuar o cadastro?\n1 - Continuar\n2 - Voltar\n"))
            if conti_cpf == 2:
                return
         
         else: 
             continuar_cpf = 0
         

        eleitor_mesario = input("Você será mesário?\n1 - Sim\n0 - Não\n")
        while eleitor_mesario not in ["0", "1"]:
            print("Digite um dos valores: 0 ou 1")
            eleitor_mesario = input("Você será mesário?\n1 - Sim\n0 - Não")

        eleitor_mesario = int(eleitor_mesario)

        chaveacesso=gerar_chave.eleitor_chave_de_acesso(nome1, nome2)
        sql = """
        INSERT INTO eleitores (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario, eleitor_chaveacesso)
        VALUES (%s, %s, %s, %s, %s)"""

        valores = (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario, chaveacesso)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Eleitor cadastrado com sucesso!")
        registro_log(f"Eleitor", "{eleitor_nome}", "cadastrado na base de dados")
        print("Sua chave de acesso é:", chaveacesso)

    except mysql.connector.Error as erro:
        if erro.errno == 1062:
            texto_erro = str(erro).lower()

            if "cpf" in texto_erro:
                registro_log("tentativa de cadastro com CPF já cadastrado na base de dados")
                print("CPF já cadastrado!")
            elif "titulo" in texto_erro:
                registro_log("tentativa de cadastro com Titulo de eleitor já cadastrado na base de dados")
                print("Título de eleitor já cadastrado!")
            else:
                registro_log("tentativa de cadastro com dados duplicados")
                print("Dado duplicado já cadastrado!")
        else:
            print("Erro no banco:", erro)

    except Exception as erro:
        print("Erro inesperado:", erro)

    finally:
        cursor.close()
        conexao.close()