class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que ten nome e idade

    Para criar uma nova pessoa, use variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): #Método construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __getstate(self):
        return f"Estado: nome = {self.nome} ; idade {self.idade}"
    
#Declaração de Objetos
g1 = Gafanhoto(nome="Maria", idade=25)
g1.aniversario()
print(g1)

print(g1.__dict__) #Attribute
print(g1.__getstate__()) #Method
print(g1.__class__)

#print(g1.__doc__) #Dunder Attribute


