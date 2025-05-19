from flask import Flask, render_template, request, redirect, url_for
from conectdb import gettasks, add_task, delete_task, toggle_task, get_task, update_task

app = Flask(__name__)

@app.route('/')
def home():
    tasklist = gettasks()
    return render_template('todolist.html', TaskList=tasklist)

@app.route('/add', methods=['POST'])
def add():
    taskname = request.form['TaskName']
    duedate = request.form['DueDate']
    add_task(taskname, duedate)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('home'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    toggle_task(task_id)
    return redirect(url_for('home'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_name = request.form['TaskName']
        new_date = request.form['DueDate']
        update_task(task_id, new_name, new_date)
        return redirect(url_for('home'))
    else:
        task = get_task(task_id)
        return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)