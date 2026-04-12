def validar_titulo(titulo):
    if titulo.isdigit() or len(titulo) != 12:
        return False
    return True

    if titulo == titulo[0] * 12:
        return False

    #Primeiro digito verificador
    soma = 0
    for i in range(8):
        soma += int(titulo[i])*(i+2)

    resto=soma%11

    if resto==0:
        dig1=0
    elif resto==1:
        dig1=0
    else:
        dig1=11-resto

    #Segundo digito verificador
    soma=0
    for i in range(8, 11):
        soma += int(titulo[i])*(i-1)

    resto=soma%11

    if resto==0:
        dig2 = 0
    elif resto==1:
        dig2=0
    else:
        dig2 = 11-resto

    #Validação final
    return dig1 == int(titulo[10]) and dig2 == int(titulo[11])

    # o calculo para fazer a validação do titulo é bem parecido 
    # com o caluculo para validar o CPF