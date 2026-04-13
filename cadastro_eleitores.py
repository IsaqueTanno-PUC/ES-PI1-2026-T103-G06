import conexaoBD
from conexaoBD import conectar
import validar
import validacao_titulo

def cadastrar_eleitor():
    """
    Realiza a leitura dos dados do eleitor, passando pelas validações do título/cpf e cria uma chave de acesso única em caso positivo de cadastro
    
    Args:
        Input do usuário dentro da função

    Returns:
        Em caso positivo, realiza o cadastro no banco de dados e gera a chave de acesso única
    
    """

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CADASTRO DE ELEITOR ===")
        eleitor_nome = input ("Digite seu nome: ")

        #verificação e validação do titulo de eleitor do usuario:
        eleitor_titulo = input ("Digite seu titulo de eleitor: ").replace(".", "").replace("-", "")
        if validacao_titulo.validar_titulo(eleitor_titulo)==False:
            print ("Titulo de Eleitor inválido!")
            return

        #essa parte depois do input de cpf "remove" os acentos do CPF (caso tiver)
        #e deixa sem pontuacao para evitar parar o programa também faz a validação do CPF do usuario
        eleitor_cpf = input ("Digite seu CPF: ").replace(".", "").replace("-", "")
        if validar.cpf(eleitor_cpf)==False:
            print ("CPF inválido!")
            return

        eleitor_mesario = input("Você será mesário?\n1 - Sim\n0 - Não")
        while eleitor_mesario not in ["0", "1"]:
            print("Digite um dos valores: 0 ou 1")
            eleitor_mesario = input("Você será mesário?\n1 - Sim\n0 - Não")

        eleitor_mesario = int(eleitor_mesario)

        sql = """
        INSERT INTO eleitores (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario)
        VALUES (%s, %s, %s, %s)"""

        valores = (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Eleitor cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar eleitor:", erro)

    finally:
        cursor.close()
        conexao.close()
