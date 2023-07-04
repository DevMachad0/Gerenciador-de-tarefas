from create_table.task_manager import TaskManager, Task

def show_menu():
    print("===== Gerenciador de Tarefas =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")
    print("==================================")

def main():
    task_manager = TaskManager("tasks.db")
    task_manager.create_table()

    while True:
        show_menu()
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            title = input("Digite o título da tarefa: ")
            description = input("Digite a descrição da tarefa: ")
            task = Task(title, description)
            task_manager.add_task(task)
            print("Tarefa adicionada com sucesso!")

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_id = input("Digite o ID da tarefa concluída: ")
            task_manager.mark_task_as_completed(task_id)
            print("Tarefa marcada como concluída!")

        elif choice == "4":
            task_id = input("Digite o ID da tarefa a ser excluída: ")
            task_manager.delete_task(task_id)
            print("Tarefa excluída!")

        elif choice == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
