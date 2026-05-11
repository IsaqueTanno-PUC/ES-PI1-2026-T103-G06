import random
import string
from datetime import datetime
from conexaoBD import conectar
from auditoria import registro_log, protocolo_votacao

def registrar_voto(eleitor_id, cand_numero):
    
    """
    Registra o voto no banco de dados.
    Args:
        eleitor_id (int): Id do eleitor que está votando.
        cand_numero (int): Número do candidato escolhido.
    Returns:
        bool: False, se não registrar o voto e True em caso afirmativo; str: Protocolo gerado.
    """
    conexao= conectar()
    cursor= conexao.cursor()

    horario= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    protocolo= "V" + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + "26" + str(cand_numero).zfill(2) + str(random.randint(10000, 99999))

    try:
        sql= "INSERT INTO votos (voto_horario, voto_candnumero, voto_protocolo) VALUES (%s, %s, %s)"
        valores= (horario, cand_numero, protocolo)
        cursor.execute(sql, valores)

        sql= "UPDATE eleitores SET eleitor_situacao= 1, eleitor_horavoto= %s WHERE eleitor_id= %s"
        valores= (horario, eleitor_id)
        cursor.execute(sql, valores)

        conexao.commit()
        registro_log("SUCESSO: Voto realizado com sucesso")
        protocolo_votacao(protocolo)
        print("Voto registrado com sucesso")
        print("Protocolo: ", protocolo)
        return True

    except Exception as erro:
        print("Erro ao registrar voto: ", erro)
        return False

    finally:
        cursor.close()
        conexao.close()

def eleitor_iniciar_voto():
    """
    Solicita as informações do eleitor que irá votar
    Args:
        Nenhum (input é interno na função)
    Returns:
        bool: False, se não houver voto; True, caso o voto tenha sido bem-sucedido
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

        sql = "SELECT eleitor_titulo, eleitor_cpf, eleitor_chaveacesso, eleitor_situacao, eleitor_id FROM eleitores WHERE eleitor_titulo = %s AND eleitor_cpf LIKE %s AND eleitor_chaveacesso = %s"
        cpf=cpf+"%" # O resto pode ser qualquer, pois só precisamos dos 4 primeiros dígitos
        aux=(titulo,cpf,chave)
        
        cursor.execute (sql, aux)
        resultado = cursor.fetchone()



        if resultado==None:
            registro_log("ALERTA: Tentativa de votação negado. Usuario não encontrado!")
            print("Não foi possível continuar! Usuário não encontrado!")
            return False
        
        elif resultado[3]==1:
            registro_log("ALERTA: Tentativa de votação negado. Eleitor já votou!")
            print("Não foi possível continuar! Eleitor já registrou o voto!")
            return False
        
        elif resultado[3]==0:
            escolha=""
            confirmar=False
            while escolha.isdigit==False or confirmar==False:  
                try:
                    numero_voto=int(input("\nDigite o número do candidato: "))
                except:
                    numero_voto=-1
                if numero_voto>0:
                    encontro=exibir_candidato(numero_voto)
                    if encontro==True:
                        escolha2=input("Deseja confirmar o voto neste candidato? [S/N] ").replace(" ", "").replace("[","").replace("]","").upper()
                        if escolha2=="S":
                            voto=registrar_voto(resultado[4],numero_voto)
                            if voto==True: confirmar=True
            return True

        return False

    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()

def exibir_candidato(n_cand):
    """
    Exibe o nome, o número e o partido de um candidato buscado pelo seu número
    Args:
        int: Número do candidato
    Returns:
        bool: False se não for encontrado e True se encontrado, além da exibição das informações do candidato
    """
    try:
        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute("""  SELECT 
                                can_nome,
                                cand_numero,
                                cand_partido
                            FROM candidatos
                            WHERE cand_numero = %s""", (n_cand,))
        candidatos=cursor.fetchone()

        if candidatos==None:
            print("CANDIDATO NÃO ENCONTRADO")
            return False
        
        else:
            nome,numero,partido=candidatos
            print(f"\nNome: {nome}")
            print(f"Número: {numero}")
            print(f"Partido: {partido}\n")
            return True

    except Exception as erro:
        print("Erro inesperado: ", erro)
    finally:
        cursor.close()
        conexao.close()