from random import randint

# cria a variavel matriz
matriz = []

#cria a linha
for l in range(0,3):
    #cria a variavel para armazenar os valores
    linha = []
    #cria as colunas
    for c in range(0,3):
        #armazena as linhas por coluna
        linha.append(randint(0,9))
    matriz.append(linha)

for linha in matriz:
    for coluna in linha:
        print(f"[{coluna}]", end='')
    print()
