from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app
db = SQLAlchemy(applications)


@app.route('/')
def index():
    return 'flask-movies 07a'


if __name__ == '__main__':
    application.run()

