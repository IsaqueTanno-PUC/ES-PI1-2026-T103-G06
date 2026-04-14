import conexaoBD
from conexaoBD import conectar
import validar
import validacao_titulo
import gerar_chave

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
        eleitor_nome = input ("Digite seu nome: ")
        nome1=""
        nome2=""
        nome=str(eleitor_nome)
        nome_nchar=len(nome)
        cont=0
        while(cont<nome_nchar and nome[cont]!=" "):
            nome1=nome1+nome[cont]
            cont=cont+1
        cont=cont+1
        while(cont<nome_nchar and nome[cont]!=" "):
            nome2=nome2+nome[cont]
            cont=cont+1
        if nome1.isalpha()==False or nome2.isalpha()==False:
            print("Nome inválido! Digite apenas com letras e, pelo menos, coloque o segundo nome")
            return

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

        chaveacesso=gerar_chave.eleitor_chave_de_acesso(nome1, nome2)
        sql = """
        INSERT INTO eleitores (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario, eleitor_chaveacesso)
        VALUES (%s, %s, %s, %s, %s)"""

        valores = (eleitor_nome, eleitor_titulo, eleitor_cpf, eleitor_mesario, chaveacesso)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Eleitor cadastrado com sucesso!")
        print("Sua chave de acesso é:", chaveacesso)

    except Exception as erro:
        print("Erro ao cadastrar eleitor:", erro)

    finally:
        cursor.close()
        conexao.close()
