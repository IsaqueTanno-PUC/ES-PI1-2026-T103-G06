def validar_titulo(titulo):
    titulo = str(titulo)

    #Validação inicial
    if not titulo.isdigit() or len(titulo) != 12:
        return False

    #Evita números repetidos
    if titulo == titulo[0] * 12:
        return False

    #Primeiro dígito verificador
    soma = 0
    for i in range(8):
        soma += int(titulo[i]) * (i + 2)

    resto = soma % 11

    if resto < 2:
        dig1 = 0
    else:
        dig1 = 11 - resto

    #Segundo dígito verificador
    soma = 0
    for i in range(8, 11):
        soma += int(titulo[i]) * (i - 1)

    resto = soma % 11

    if resto < 2:
        dig2 = 0
    else:
        dig2 = 11 - resto

    # Validação final
    return dig1 == int(titulo[10]) and dig2 == int(titulo[11])

    # o calculo para fazer a validação do titulo é bem parecido 
    # com o caluculo para validar o CPF