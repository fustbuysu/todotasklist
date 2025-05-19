import psycopg2

db_name = 'tasklistdb'
db_user = 'postgres'
db_pw = '1'
db_host = 'localhost'

def get_connection():
    return psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)

def gettasks():
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('SELECT id, task_name, is_active, due_date FROM tasklist ORDER BY id')
    tasks = curs.fetchall()
    curs.close()
    connect.close()
    return tasks

def get_task(task_id):
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('SELECT id, task_name, is_active, due_date FROM tasklist WHERE id = %s', (task_id,))
    task = curs.fetchone()
    curs.close()
    connect.close()
    return task

def add_task(name, date):
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('INSERT INTO tasklist (task_name, due_date) VALUES (%s, %s)', (name, date))
    connect.commit()
    curs.close()
    connect.close()

def delete_task(task_id):
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('DELETE FROM tasklist WHERE id = %s', (task_id,))
    connect.commit()
    curs.close()
    connect.close()

def toggle_task(task_id):
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('UPDATE tasklist SET is_active = NOT is_active WHERE id = %s', (task_id,))
    connect.commit()
    curs.close()
    connect.close()

def update_task(task_id, name, date):
    connect = get_connection()
    curs = connect.cursor()
    curs.execute('UPDATE tasklist SET task_name = %s, due_date = %s WHERE id = %s', (name, date, task_id))
    connect.commit()
    curs.close()
    connect.close()