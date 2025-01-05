import sqlite3

def db_connect():
    conn = sqlite3.connect('task_manager.db')
    return conn

# def create_table():
#     conn = db_connect()
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
#         id INTEGER PRIMARY KEY NOT NULL,
#         title VARCHAR(50),
#         description VARCHAR(255),
#         complated BOOLEAN DEFAULT False
#     )''')
#     conn.commit()
#     conn.close()

def get_all_tasks():
    conn = db_connect()
    cursor = conn.cursor()
    tasks = cursor.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return tasks

def create_task(title, description):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()

def task_complete(task_id, complete):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET complated=? WHERE id=?', (complete, task_id))
    conn.commit()
    conn.close()

def task_delete(task_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
