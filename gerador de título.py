# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:38:06 2026

@author: madu
"""

import random

def gerar_titulo_valido():
    base = ""

    # gera 10 dígitos aleatórios
    for i in range(10):
        base += str(random.randint(0, 9))

    # evita todos iguais (ex: 1111111111)
    if base == base[0] * 10:
        return gerar_titulo_valido()

    # cálculo do primeiro dígito
    soma = 0
    for i in range(8):
        soma += int(base[i]) * (i + 2)

    resto = soma % 11
    dig1 = 0 if resto == 10 else resto

    # cálculo do segundo dígito
    titulo_parcial = base + str(dig1)

    soma = 0
    for i in range(8, 11):
        soma += int(titulo_parcial[i]) * (i - 1)

    resto = soma % 11
    dig2 = 0 if resto == 10 else resto

    return base + str(dig1) + str(dig2)


# teste
for i in range(5):
    print(gerar_titulo_valido())