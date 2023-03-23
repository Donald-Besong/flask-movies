from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'flask-movies 06'


application = app
if __name__ == '__main__':
    application.run()

