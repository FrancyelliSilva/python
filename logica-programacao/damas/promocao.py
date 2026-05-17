def verificar_promocao(pecas_brancas, pecas_pretas):
    """ Verifica se alguma peça deve ser promovida a dama. 
    Args:
        pecas_brancas (list): Lista de peças brancas.
        pecas_pretas (list): Lista de peças pretas.
    
    Returns:
        pecas_brancas (list): Lista atualizada de peças brancas.
        pecas_pretas (list): Lista atualizada de peças pretas.
    """
    #verificar promoção das peças brancas
    for pb in pecas_brancas:
        if pb[1][0] == 0 and pb[2] != 'dama':
            pb[2] = 'dama'
            print(f"Peça {pb[0]} promovida a dama!")

    #verificar promoção das peças pretas
    for pp in pecas_pretas:
        if pp[1][0] == 7 and pp[2] != 'dama':
            pp[2] = 'dama'
            print(f"Peça {pp[0]} promovida a dama!")
            
    return pecas_brancas, pecas_pretas