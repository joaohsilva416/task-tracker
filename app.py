# Libs necessárias
import sys
import os

# Função para adicionar tarefa
def add_task():
    pass


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