from promocao import verificar_promocao

pecas_brancas = [
    ['b01', [5, 0], 'dama'], ['b02', [5, 2], 'peão'], ['b03', [5, 4], 'peão'], ['b04', [5, 6], 'peão'],
    ['b05', [6, 1], 'peão'], ['b06', [6, 3], 'peão'], ['b07', [6, 5], 'peão'], ['b08', [6, 7], 'peão'],
    ['b09', [7, 0], 'peão'], ['b10', [7, 2], 'peão'], ['b11', [7, 4], 'peão'], ['b12', [7, 6], 'peão']
    ]


pecas_pretas = [
    ['p01', [0, 1], 'peão'], ['p02', [0, 3], 'peão'], ['p03', [0, 5], 'peão'], ['p04', [0, 7], 'peão'],
    ['p05', [1, 0], 'peão'], ['p06', [1, 2], 'peão'], ['p07', [1, 4], 'peão'], ['p08', [1, 6], 'peão'],
    ['p09', [2, 1], 'dama'], ['p10', [2, 3], 'peão'], ['p11', [2, 5], 'peão'], ['p12', [2, 7], 'peão']
    ]

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
    else:
        matriz[linha][coluna] = "○"

#adicionar peças pretas no tabuleiro
for pp in pecas_pretas:
    linha = pp[1][0]
    coluna = pp[1][1]
    tipo = pp[2]

#adicionar damas pretas no tabuleiro
    if tipo == 'dama':
        matriz[linha][coluna] = "▲"
    else:
        matriz[linha][coluna] = "●"


#imprimir tabuleiro
print("\nTabuleiro:")
print("Legenda: ● = peão preto | ▲ = dama preta | ○ = peão branco | △ = dama branca\n")
print("  0 1 2 3 4 5 6 7")
print(" -----------------")

for i, linha in enumerate(matriz):
    print(f"{i}|", end=" ")
    for elemento in linha:
        print(elemento, end=" ")
    print()
print(" -----------------")
