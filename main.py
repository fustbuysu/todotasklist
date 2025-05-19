from flask import Flask, render_template

app = Flask(__name__)

tasklist = [['walk dog', True], ['wash dishes', False]]
@app.route('/')
def home():
    return render_template('todolist.html', TaskList=tasklist)

app.run()