# Libs necessárias
import sys
import os
import json
from datetime import datetime

# Função para adicionar tarefa
def add_task():
    command = sys.argv[2] # Comando para o CLI
    # Verifica se o arquivo json existe
    if os.path.exists('tasks.json'):
        # Se existir abre o arquivo e carrega as tarefas
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    
    # Se não existir inicia uma lista vazia
    else:
        tasks = []
    
    # Abre o arquivo JSON para escrita
    with open("tasks.json", "w") as file:
        # Adiciona a tarefa na lista de tarefas
        tasks.append({
            "id": len(tasks) + 1,
            "description": command,
            "status": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Escreve as tarefas no arquivo JSON
        json.dump(tasks, file, indent=4)
        print(f"Task added succesfully (ID: {len(tasks)})")


# Função para atualizar tarefa
def update_task():
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]

    # 1. Carrega o arquivo json com as tarefas
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    
    # 2. Modifica o dado (description) da tarefa com o id informado
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Escreve as tarefas atualizadas no arquivo json
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
                print(f"Task {task_id} updated succesfully")
            break
    else:
        print(f"Task {task_id} not found.")


# Função para excluir tarefa
def delete_task():
    task_id = int(sys.argv[2])

    # 1. Carrega o arquivo json com as tarefas
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    
    # 2. Filtra as tarefas que não serão excluídas
    filtered_tasks = [task for task in tasks if task["id"] != task_id]

    # 3. Verifica se o ID existe ou não
    if len(tasks) == len(filtered_tasks):
        print(f"Task {task_id} not found.")
    
    else:
        # 3. Escreve as tarefas filtradas no arquivo json
        with open("tasks.json", "w") as file:
            json.dump(filtered_tasks, file, indent=4)
            print(f"Task {task_id} deleted succesfully")


# Função para listar tarefas por status
def list_tasks_by_status(status):
    pass


# Função para marcar tarefa como em progresso
def mark_task_as_in_progress():
    task_id = int(sys.argv[2])
    in_progress = "in-progress"

    # 1. Carrega o arquivo json com as tarefas
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    # 2. Muda o status da tarefa para "in-progress"
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = in_progress
            # Escreve as tarefas no arquivo json
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
                print(f"Task {task_id} marked as in-progress.")
            break
    else:
        print(f"Task {task_id} not found.")  


# Função para marcar tarefa como concluida
def mark_task_as_done():
    task_id = int(sys.argv[2])
    done = "done"

    # 1. Carrega o arquivo json com as tarefas
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    # 2. Muda o status da tarefa para "done"
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = done
            # Escreve as tarefas no arquivo json
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
                print(f"Task {task_id} marked as done.")
            break
    else:
        print(f"Task {task_id} not found.")


# Estrutura do CLI
command = sys.argv[1]
commands = {
    "add": add_task,
    "update": update_task,
    "delete": delete_task,
    "list": list_tasks_by_status,
    "mark-done": mark_task_as_done,
    "mark-in-progress": mark_task_as_in_progress,
}

# Executa a função correspondente ao comando informado pelo usuário
operation_function = commands[command]
operation_function()