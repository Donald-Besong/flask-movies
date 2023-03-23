from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

#from app import db

tasklist_blueprint = Blueprint('tasklist', __name__)


@tasklist_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return 'flask-movies 8'


