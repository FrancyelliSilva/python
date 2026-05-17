lista = []
n = 0
while n != 4:
    print('-----MENU---------')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')
    n = int(input())

    match n:
        case 1:
            print("Digite a tarefa: ")
            nova_tarefa = input()
            lista.append(nova_tarefa)
        case 2:
            for l, tarefa in enumerate(lista):
                print(f"{l} - {tarefa}")
        case 3:
            print("Digite a o número da tarefa que deseja remover: ")
    print(lista)


