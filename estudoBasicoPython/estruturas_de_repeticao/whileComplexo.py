tarefas = []
print("escolha uma das opcoes baixo")
print('1-adicionar tarefa')
print('2-remover tarefa')
print('3-mostrar tarefa')
print('4-sair')

while True:
    print("escolha uma das opcoes baixo")
    print('1-adicionar tarefa')
    print('2-remover tarefa')
    print('3-mostrar tarefa')
    print('4-sair')

    escolha = input("digite o numero da funcao desejada: ")

    if escolha == "1":
        tarefa = input("digite a tarefa desejada: ")
        tarefas.append(tarefa)

    elif escolha == "2":
        print(f"{tarefas}")
        remover = input("escolha a tarefa para remover ")
        tarefas.remove(remover)

    elif escolha == "3":
        print(f"as tarefas sao: {tarefas}")
        print(f"o numero de tarefas sao: {len(tarefas)}")

    elif escolha == "4":
        print("encerrando programa...")
        break

    else:
        print('opcao invalida')
