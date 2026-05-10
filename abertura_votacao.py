import conexaoBD
from conexaoBD import conectar
import zerezima
import auditoria
from auditoria import registro_log

def abrir_votacao():
    """
    Solicita as informações do mesário e executa a função do zerezima
    Args:
        Nenhum
    Returns:
        bool: True se for bem sucedido e False se houver algum cancelamento, erro, ou eleitor não é mesário
    """
    try:
        conexao=conectar()
        cursor=conexao.cursor()
        
        print("Digite CANCELAR caso deseje sair deste processo")
        titulo="a"
        while len(titulo)!=12 or titulo.isdigit()==False:
            try:
                titulo=input("Digite o título de eleitor: ").strip()
                if titulo.upper()=="CANCELAR":
                    print("Processo cancelado...")
                    return False

                elif len(titulo)!=12 or titulo.isdigit()==False:
                    print("\nErro! Digite um título válido!")
            except:
                titulo="a"
                print("\nErro! Digite um título válido!")

        cpf="a"
        while len(cpf)!=4 or cpf.isdigit()==False:
            try:
                cpf=input("Digite os 4 primeiros dígitos do cpf: ").replace(".", "").strip()
                if cpf.upper()=="CANCELAR":
                    print("Processo cancelado...")
                    return False
                
                elif len(cpf)!=4 or cpf.isdigit()==False:
                    print("\nErro! Digite 4 dígitos válidos!")
            except:
                cpf="a"
                print("\nErro! Digite 4 dígitos válidos!")

        chave="a"
        while len(chave)!=7:
            try:
                chave=input("Digite a chave de acesso: ").strip()
                if chave.upper()=="CANCELAR":
                    registro_log("Operação de abertura de votação cancelada pelo usuario")
                    print("Processo cancelado...")
                    return False
                
                elif len(chave)!=7:
                    print("\nErro! Digite uma chave de acesso válida!")
            except:
                chave="a"
                print("\nErro! Digite uma chave de acesso válida!")

        sql = "SELECT eleitor_titulo, eleitor_cpf, eleitor_chaveacesso, eleitor_mesario FROM eleitores WHERE eleitor_titulo = %s AND eleitor_cpf LIKE %s AND eleitor_chaveacesso = %s"
        cpf=cpf+"%" # O resto pode ser qualquer, pois só precisamos dos 4 primeiros dígitos
        aux=(titulo,cpf,chave)
        
        cursor.execute (sql, aux)
        resultado = cursor.fetchone()



        if resultado==None:
            registro_log("ALERTA: Tentativa de acesso negado\nUsuario não encontrado!")
            print("Não foi possível abrir o sistema de votação! Usuário não encontrado!")
            return False
        
        elif resultado[3]==0:
            registro_log("ALERTA: Tentativa de acesso negado\nEleitor não é mesário!")
            print("Não foi possível abrir o sistema de votação! Eleitor não é mesário!")
            return False
        
        elif resultado[3]==1:       # O sistema é aberto aqui
            zerezima.zerar_votos()
            zerezima.listar_candidatos()
            registro_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
            x=input("\nZerézima realizado! Sistema de votação será iniciado. Pressione ENTER para continuar ")
            return True

        return False

    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()