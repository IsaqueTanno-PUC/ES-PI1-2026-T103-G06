import menu
import conexaoBD
import cadastro_eleitores
import busca_eleitores
import listagemeleitores
import remocao_eleitores

escolha1,escolha2,escolha3=-1,-1,-1

while(escolha1!=3):
    escolha1=-1
    # Menu HOME (principal)
    print("\nSISTEMA DE VOTAÇÃO LAD.Py\n")

    print("1 - Gerenciamento")
    print("2 - Sistema de Votação")
    print("3 - Sair")
    escolha1 = menu.number_option_input(1,3)
    escolha2=-1
    match escolha1:
        case 1:
            while(escolha2!=6):
                escolha2=-1
                # Gerenciamento
                print("\nGERENCIAMENTO\n")
                print("1 - Cadastro de Eleitores")
                print("2 - Editar dados de Eleitoes")
                print("3 - Remover Eleitor")
                print("4 - Buscar Eleitor por título/CPF")
                print("5 - Listagem de Eleitores")
                print("6 - Voltar")
                escolha2 = menu.number_option_input(1,6)
                #após o usuario escolher 1 (cadastro de eleitor) essa opcao leva para cadastro_eleitores
                #onde é possivel realizar o cadastro de um novo eleitor
                if escolha2 ==1:
                    cadastro_eleitores.cadastrar_eleitor()
                if escolha2 == 3:
                    remover_eleitor.remover_eleitor()
                if escolha2 == 4:
                    busca_eleitores.busca_eleitor()
                if escolha2 == 5:
                    listagemeleitores.listar_eleitores()

        case 2:
            while(escolha2!=4):
                escolha2=-1
                # Sistema de Votação
                print("\nSistema de Votação\n")
                print("1 - Abrir Sistema de Votação")
                print("2 - Auditoria do Sistema")
                print("3 - Resultados da Votação")
                print("4 - Voltar")
                escolha2 = menu.number_option_input(1,4)
                escolha3 = -1
                match escolha2:
                    case 1:
                        while(escolha3!=2):
                            escolha3=-1
                            print("\nSistema de Votação")
                            print("1 - Votar")
                            print("2 - Fechar Sistema de Votação")
                            escolha3= menu.number_option_input(1,2)
                    case 2:
                        while(escolha3!=3):
                            escolha3=-1
                            print("\nAuditoria")
                            print("1 - Logs de Ocorrência")
                            print("2 - Protocolos de Votação")
                            print("3 - Voltar")
                            escolha3= menu.number_option_input(1,3)
                    case 3:
                        while(escolha3!=5): # Resultados da Votação
                            escolha3=-1
                            print("\nResultados da Votação:")
                            print("1 - Validação de integridade")
                            print("2 - Boletim de Urna")
                            print("3 - estatistica de comparecimento")
                            print("4 - Votos por partido")
                            print("5 - Voltar")
                            escolha3= menu.number_option_input(1,5)
        case 3:
            print("\nSaindo do Sistema...")
