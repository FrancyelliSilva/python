class Arvore:

    def __init__(self, no):
        self.raiz = no

    def adicionar_no(self, no_pai, no_filho): 
        no_pai.filhos.append(no_filho) #adicionar nó filho
    
    def dfs(self, no, callback): #busca em profundidade
        callback(no) #print
        for filho in no.filhos: #verifica se há filhos
            self.dfs(filho, callback)
    
    def bfs(self, callback): #no momento que chama o bfs é criado uma lista - busca em largura
        fila = deque() 
        fila.append(self.raiz)
        while fila: #enquanto a fila estiver ocupada, caso não tenha nenhum elemento, a função é finalizada
            no_atual = fila.popleft() #retira o primeiro da fila
            callback(no_atual) #imprimi o que esta saindo
            for filho in no_atual.filhos: # para cada filho que tem nó
                fila.append(filho) # o nó é adicionado na fila

    def imprimir_hierarquia(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        
        print(" " * nivel + str(no.valor)) #string vazia x nivel da arvore + o valor do nó

        for filho in no.filhos: #para cada filho que tiver dentro nó que esta sendo verificado
            self.imprimir_hierarquia(filho, nivel + 1)


