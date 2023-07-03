import sqlite3

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self, database):
        self.database = database

    def create_table(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, completed INTEGER)")
        conn.commit()
        conn.close()

    def add_task(self, task):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)", (task.title, task.description, 0))
        conn.commit()
        conn.close()

    def list_tasks(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()

        if tasks:
            for task in tasks:
                task_id, title, description, completed = task
                status = "Concluída" if completed else "Pendente"
                print(f"[{task_id}] - {title} - {description} - {status}")
        else:
            print("Nenhuma tarefa encontrada.")

    def mark_task_as_completed(self, task_id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (1, task_id))
        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
