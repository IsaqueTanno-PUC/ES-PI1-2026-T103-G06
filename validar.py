def cpf(cpf):
    """
    Lê o valor do CPF e retorna em booleano se é válido ou não

    Args:
        cpf(string): O número do CPF a ser validado, formato: 11111111122

    Returns;
        bool: true se o cpf for válido e false se for inválido
    """
    cpf=str(cpf)
    nchar=len(cpf)

    # Testar se tem mais ou menos caracteres (não permitido)
    if nchar!=11:
        return False
    else:
        # Testar se todos os números são iguais (não permitido). O contador começa a testar a partir do segundo dígito
        cont=1
        niguais=0
        while cont<nchar:
            if cpf[0] == cpf[cont]:
                niguais=niguais+1
            cont=cont+1
        if niguais==10:
            return False
        else:

            # Cálculo dígito 1
            cont=0
            soma=0
            while cont<9:
                soma=soma+(int(cpf[cont]))*(10-cont)
                cont=cont+1
            if (soma%11) < 2:
                dgtver1=0
            else:
                dgtver1=11-(soma %11)
            
            # Cálculo dígito 2
            cont=0
            soma=0
            while cont<9:
                soma=soma+(int(cpf[cont]))*(11-cont)
                cont=cont+1
            soma=soma+dgtver1*2
            dgtver2=11-(soma%11)

            # Verificar se é válido (dígitos são os mesmos)
            if int(cpf[9])==dgtver1 and int(cpf[10])==dgtver2:
                return True
            else:
                return False

