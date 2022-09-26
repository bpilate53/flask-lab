from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from todo.models import Task

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    all_tasks = Task().get_all()
    return render_template('todo/index.html', tasks = all_tasks)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_task = Task().create()
        return redirect(url_for('todo.index'))

    return render_template('todo/create.html')
    


@bp.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    task = Task().get_one(name)
    
    if request.method == 'POST':
        task = Task().update()
        return redirect(url_for('todo.index'))
        
    return render_template('todo/update.html', task = task)

@bp.route('/delete/<name>', methods=['POST'])
def delete(name):
    delete = Task().delete(name)
    return redirect(url_for('todo.index'))

    