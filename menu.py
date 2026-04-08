def number_option_input(opcao_min, opcao_max):
     """
    Validar input do usuário entre dois valores, diante de um menu numérico

    Args:
        opcao_min(int): O menor número disponível para escolha no menu
        opcao_max(int): O maior número disponível para escolha no menu
    
    Returns:
        int: opção válida escolhida pelo usuário
    """
     opcao = -1
     while (opcao < opcao_min or opcao > opcao_max):
        try:
            
            opcao = int(input("\nDigite sua opção: "))
        except:
            
            print("Erro! Digite um valor numérico")
        else:
            
            if opcao >= opcao_min and opcao <= opcao_max:
                return opcao
            else:
                
                print(f"Erro! Digite um valor entre {opcao_min} e {opcao_max}")