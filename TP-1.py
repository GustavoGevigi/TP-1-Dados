taskList = [{"name": "Pesquisa Experimental", "completed": False},
            {"name": "Análise de Dados", "completed": False},
            {"name": "Manutenção de Equipamentos", "completed": False},
            {"name": "Colaboração Científica", "completed": False},
            {"name": "Aulas ou Treinamentos", "completed": False},
            {"name": "Revisão de Literatura Científica", "completed": False},
            {"name": "Supervisão de Estagiários e Assistentes", "completed": False},
            {"name": "Preparação de Relatórios Científicos", "completed": False},
            {"name": "Participação em Simulações e Treinamentos de Emergência", "completed": False},
            {"name": "Cumprir Procedimentos de Segurança", "completed": False},]



def showMenu():
    menu = """
    Task+

    1. Adicionar nova Tarefa
    2. Listar Tarefas
    3. Marcar concluída
    4. Deletar Tarefas
    """
    print(menu)


def addTask():
    taskName = input("Informe o nome da tarefa a ser adicionada: ")
    taskList.append({"name": taskName, "completed": False})
    print(f"Tarefa {taskName} adicionada na lista de tarefas")
    input("Pressione ENTER para continuar...")


def ListAllTasks():
    print("Tarefas presentes na lista de tarefas: ")
    listNum = 1
    for task in taskList:
        status = "Concluída" if task["completed"] else "Pendente"
        print(f"{listNum}: {task['name']} - {status}")
        listNum += 1


def MarkCompleted():
    ListAllTasks()
    userInput = input("Digite o número da tarefa a ser concluída: ")

    try:
        indexValue = int(userInput) - 1

        if 0 <= indexValue < len(taskList):
            taskList[indexValue]["completed"] = True
            print("Tarefa marcada como concluída com sucesso!")
        else:
            print("Índice inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


def DeleteTask():
    ListAllTasks()
    userInput = input("Digite o número da tarefa desejada para deletar: ")

    try:
        indexValue = int(userInput) - 1

        if 0 <= indexValue < len(taskList):
            removedTask = taskList.pop(indexValue)
            print(f"Tarefa {removedTask['name']} removida com sucesso")
        else:
            print("Índice inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


while True:
    showMenu()

    userInput = input("Digite o número da opção desejada: ")

    if userInput == '1':
        addTask()
    elif userInput == '2':
        ListAllTasks()
    elif userInput == '3':
        MarkCompleted()
    elif userInput == '4':
        DeleteTask()
    elif userInput == '0':
        print("Encerrando aplicação...")
        break
    else:
        print("Opção inválida, tente novamente")
