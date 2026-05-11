from conexaoBD import conectar
import validar
import validacao_titulo
from auditoria import registro_log

def editar_eleitor_menu():
    conexao=conectar()
    cursor=conexao.cursor()

    try:
        CPF_eleitor = input("Digite o CPF do eleitor: ")
        CPF_eleitor = CPF_eleitor.replace(".", "").replace("-", "")
        CPF_eleitor =int(CPF_eleitor)
    except ValueError:
        print("CPF Inválido!")
        return

    cursor.execute("SELECT * FROM eleitores WHERE eleitor_cpf = %s", (CPF_eleitor,))
    eleitor = cursor.fetchone()

    if not eleitor:
        print("Eleitor não encontrado.")
        return

    print("\n Dados atuais:")
    print(f"ID: {eleitor[0]}")
    print(f"Nome: {eleitor[1]}")
    print(f"Titulo: {eleitor[2]}")
    print(f"Cpf: {eleitor[3]}")
    print(f"Mesario: {eleitor[4]}")

    print("\nO que deseja alterar?\n")
    print("1 - Nome")
    print("2 - Titulo")
    print("3 - Cpf")
    print("4 - Opcao Mesario")
    print("5 - sair")

    fsaida=0
    while(fsaida == 0):
        opcao = input("Escolha uma opção: ")
        errado=True
        novo_valor=""
        campo=""
        if opcao == "1":
            novo_valor = input("Novo nome: ")
            campo = "eleitor_nome"

            nome1=""
            nome2=""
            nome=str(novo_valor)
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
                registro_log("Nome invalido durante atualização do cadastro do eleitor.")
                print("Nome inválido! Digite apenas com letras e, pelo menos, coloque o segundo nome")
                errado=True
            else:
                errado=False

        elif opcao == "2":
            novo_valor = input("Novo Titulo: ")
            campo = "eleitor_titulo"
            if validacao_titulo.validar_titulo(novo_valor)==False:
                print("Titulo Inválido")
                errado=True
            else:
                errado=False

        elif opcao == "3":
            try:
                novo_valor = input("Novo Cpf: ")
                novo_valor = novo_valor.replace(".", "").replace("-", "")
                novo_valor = int(novo_valor)
                novo_valor = str(novo_valor)
                campo = "eleitor_cpf"
                if validar.cpf(novo_valor)==False:
                    print("CPF Inválido")
                    errado=True
                else:
                    errado=False
            except ValueError:
                print("CPF inválido! Digite apenas números.")
                errado=True

        elif opcao == "4":
            novo_valor = input("Atualização de opcao de mesario: ")
            campo = "eleitor_mesario"
            if novo_valor != "1" and novo_valor != "0":
                print("Digite um valor válido!! (0 ou 1)")
                errado=True
            else:
                errado=False
                novo_valor = bool(int(novo_valor))

        elif opcao == "5":
            fsaida=1
            return

        else:
            print("Opção inválida.")

        if errado != True:
            sql = f"UPDATE eleitores SET {campo} = %s WHERE eleitor_cpf = %s"
            cursor.execute(sql, (novo_valor, CPF_eleitor))
            conexao.commit()
            atualizado = cursor.rowcount > 0
            if atualizado:
                registro_log(f"Eleitor {eleitor[1]} atualizado na base de dados.")
                print("Dados atualizados com sucesso!")
            else:
                print("Nenhuma alteração foi feita.")

    cursor.close()
    conexao.close()