from promocao import verificar_promocao

def criar_tabuleiro_front(tabuleiro_back, pecas_brancas, pecas_pretas):
    # Criar uma visualização do tabuleiro para printar com base no tabuleiro back
    # Recebe uma matriz contendo o tabuleiro com código:
    # '000' casa vazia
    # 'b01' casa com uma peça branca
    # 'p01' casa com uma peça preta
    # Recebe as matrizes de peças para identificar as damas e peões
    # "□" para casa vazia
    # "△" para dama branca
    # "○" para peão branco
    # "▲" para dama preta
    # "●" para peão preto
    # Retorna uma matriz contendo o tabuleiro com as figuras correspondentes
    #cria uma matriz vazia
    matriz = []
    for i in range(8):
        linha = []
        for j in range(8):
            linha.append("□")
        matriz.append(linha)

    #função para verificar promoção
    pecas_brancas, pecas_pretas = verificar_promocao(pecas_brancas, pecas_pretas)

    #adicionar peças brancas  na tabuleiro
    for pb in pecas_brancas:
        linha = pb[1][0]
        coluna = pb[1][1]
        tipo = pb[2]

    #adicionar damas brancas no tabuleiro
        if tipo == 'dama':
            matriz[linha][coluna] = "△"
        elif tipo == 'peão':
            matriz[linha][coluna] = "○"
            

    #adicionar peças pretas no tabuleiro
    for pp in pecas_pretas:
        linha = pp[1][0]
        coluna = pp[1][1]
        tipo = pp[2]

    #adicionar damas pretas no tabuleiro
        if tipo == 'dama':
            matriz[linha][coluna] = "▲"
        elif tipo == 'peão':
            matriz[linha][coluna] = "●"
    
    return matriz

def exibir_tabuleiro(tabuleiro_back):
    # Recebe o tabuleiro codificado
    # Transforma o tabuleiro codificado em um tabuleiro com figuras
    #imprimir tabuleiro
    print("\nTabuleiro:")
    print("Legenda: ● = peão preto | ▲ = dama preta | ○ = peão branco | △ = dama branca\n")
    print("  0 1 2 3 4 5 6 7")
    print(" -----------------")

    for i, linha in enumerate(tabuleiro_back):
        print(f"{i}|", end=" ")
        for elemento in linha:
            print(elemento, end=" ")
        print()
    print(" -----------------")

# gerar a visualização e imprimir
tabuleiro_visual = criar_tabuleiro_front(tabuleiro_back, pecas_brancas, pecas_pretas)
exibir_tabuleiro(tabuleiro_visual)