from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app import db
tasklist_blueprint = Blueprint('tasklist', __name__)
from app.models import Task

@tasklist_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return 'flask-movies 8.0.0'

@tasklist_blueprint.route('/greeting/<task>', methods=['GET', 'POST'])
def greeting(task):     
    return 'Hello from tasklist {}!'.format(task)

@tasklist_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    name = "donald"
    db.session.add(Task(name=name))
    db.session.commit()

    tasks = Task.query.all()
    x = tasks[0].name
    return redirect(url_for('tasklist.greeting', task=x))


