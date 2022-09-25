from crypt import methods
from flask import Flask, Blueprint, render_template, url_for
from todo.models import Task

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    return render_template('todo/index.html')

@bp.route('/create', methods=['GET'])
def create():
    return Task().create()