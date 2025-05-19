from flask import Flask, render_template, request, redirect, url_for
from conectdb import gettasks, add_task
app = Flask(__name__)

# tasklist = [['walk dog', True], ['wash dishes', False]]

@app.route('/')
def home():
    tasklist = gettasks()
    return render_template('todolist.html', TaskList=tasklist)

@app.route('/add', methods =['POST'])
def add():
    taskname = request.form['TaskName']
    duedate = request.form['DueDate']
    add_task(taskname, duedate)
    return redirect(url_for('home'))
app.run()