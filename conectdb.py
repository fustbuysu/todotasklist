import psycopg2

db_name = 'tasklistdb'
db_user = 'postgres'
db_pw = '1'
db_host = 'localhost'

def gettasks():
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    curs = connect.cursor()
    curs.execute('SELECT id, task_name, is_active FROM tasklist')
    tasks = curs.fetchall()
    curs.close
    connect.close
    return tasks

def add_task(name, date):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    curs = connect.cursor()
    curs.execute('INSERT INTO public."tasklist"(task_name, due_date) VALUES ( \'%s\', \'%s\') ;commit;' %(name,date))
    curs.close
    connect.close