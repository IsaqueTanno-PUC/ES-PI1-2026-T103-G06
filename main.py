import menu
escolha1,escolha2,escolha3=-1,-1,-1


while(escolha1!=4):
    escolha1=-1
    # Menu HOME (principal)
    print("\nSISTEMA DE VOTAÇÃO LAD.Py\n")

    print("1 - Gerenciar Eleitores")
    print("2 - Resultados e Auditoria")
    print("3 - Iniciar Sistema de Votação")
    print("4 - Sair")
    escolha1 = menu.number_option_input(1,4)

    match escolha1:
        case 1:
            while(escolha2!=6):
                escolha2=-1
                # Gerenciamento de Eleitores
                print("\nGERENCIAMENTO DE ELEITORES\n")
                print("1 - Cadastro de Eleitores")
                print("2 - Editar dados de Eleitoes")
                print("3 - Remover Eleitor")
                print("4 - Buscar Eleitor por título/CPF")
                print("5 - Listagem de Eleitores")
                print("6 - Voltar")
                escolha2 = menu.number_option_input(1,6)
        case 2:
            while(escolha2!=4):
                escolha2=-1
                # Resultados e Auditoria
                print("\nRESULTADOS E AUDITORIA\n")
                print("1 - Resultados da Votação")
                print("2 - Auditoria: Logs de Ocorrência")
                print("3 - Auditoria: Protocolos de Votação")
                print("4 - Voltar")
                escolha2 = menu.number_option_input(1,4)
        case 3:
            while(escolha2!=2):
                escolha2=-1
                # Iniciar Sistema de Votação
                print("\nINICIAR SISTEMA DE VOTAÇÃO\n")
                print("1 - Login")
                print("2 - Voltar")
                escolha2 = menu.number_option_input(1,2)
        case 4:
            print("\nSaindo do Sistema...")