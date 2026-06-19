from Arvore import Arvore
from No import No

no_raiz = No("A")
arvore = Arvore(no_raiz)

no_B = No("B") #cria nó B
no_C = No("C") #cria nó C

arvore.adicionar_no(no_raiz, no_B) #adiciona filho B em no_raiz("A")
arvore.adicionar_no(no_raiz, no_C) #adiciona filho C em no_raiz("A")

no_D = No("D") #cria nó D
no_E = No("E") #cria nó E

arvore.adicionar_no(no_B, no_D)  #adiciona filho D em B
arvore.adicionar_no(no_B, no_E) #adiciona filho E em B

no_F = No("F")

arvore.adicionar_no(no_C, no_F)

arvore.dfs(no_raiz, print)