
class Lista:
    def __init__(self):
        self.pacientes = []
    
    def __str__ (self):
        return f"Nome: {self.nome}, Sintoma: {self.sintoma}, Prioridade: {self.prioridade}"

    def cadastrar_paciente(self, nome, sintoma, prioridade):
        paciente = {
            "nome": nome,
            "sintoma": sintoma,
            "prioridade": prioridade
        }
        self.pacientes.append(paciente)
    
    def listar_pacientes(self):
        print("\n==== PRIORIDADE ALTA ====")
        for paciente in self.pacientes:
            if paciente["prioridade"] == "alta":
                print(f"Nome: {paciente['nome']}")
                print(f"Sintoma: {paciente['sintoma']}")
        print("\n==== PRIORIDADE MÉDIA ====")
        for paciente in self.pacientes:
            if paciente["prioridade"] == "média":
                print(f"Nome: {paciente['nome']}")
                print(f"Sintoma: {paciente['sintoma']}")
        print("\n==== PRIORIDADE BAIXA ====")
        for paciente in self.pacientes:
            if paciente["prioridade"] == "baixa":
                print(f"Nome: {paciente['nome']}")
                print(f"Sintoma: {paciente['sintoma']}")

cadastro = Lista()

cadastro.cadastrar_paciente("Eduardo do KLB", "Convulsão", "alta")
cadastro.cadastrar_paciente("Marcelo Tramick", "Afundamento craniano", "alta")
cadastro.cadastrar_paciente("Nathan Carvalho", "Sangue na urina", "alta")
cadastro.cadastrar_paciente("Victor Won", "Vômito com presença de sangue", "alta")
cadastro.cadastrar_paciente("Bruna Guerra", "Convulsão", "alta")

cadastro.cadastrar_paciente("Francielly Happy", "Febre", "média")
cadastro.cadastrar_paciente("Gregorio Berlotti", "Sangramento", "média")
cadastro.cadastrar_paciente("Pedro Resende", "Febre", "média")
cadastro.cadastrar_paciente("Raphael Dudu", "Dor no olho esquerdo", "média")
cadastro.cadastrar_paciente("Francisco Duarte", "Tontura", "média")

cadastro.cadastrar_paciente("Yzabeli Torvald", "Dor de dente", "baixa")
cadastro.cadastrar_paciente("Junior Castella", "Preguiça", "baixa")
cadastro.cadastrar_paciente("Debora Mollari", "Dor de cabeça", "baixa")
cadastro.cadastrar_paciente("Larissa Gonzaga", "Dor de dente", "baixa")

while True:
    print("\n------CADASTRO DE PACIENTES----")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Excluir um paciente")
    print("4 - Modificar o nome do paciente")
    print("5 - Modificar o sintoma do paciente")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do paciente: ")
        sintoma = input("Digite o sintoma do paciente: ")
        prioridade = input("Digite a prioridade do paciente: ")
        cadastro.cadastrar_paciente(nome, sintoma, prioridade)
        
    elif opcao == 2:
            cadastro.listar_pacientes()

