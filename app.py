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
    pass


# Função para excluir tarefa
def delete_task():
    pass


# Função para listar tarefas por status
def list_tasks_by_status(status):
    pass


# Função para marcar tarefa como concluida
def mark_task_as_done():
    pass


# Função para marcar tarefa como em progresso
def mark_task_as_in_progress():
    pass


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

operation_function = commands[command]
operation_function()