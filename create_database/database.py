import sqlite3

def create_table(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, completed INTEGER)")
    conn.commit()
    conn.close()
