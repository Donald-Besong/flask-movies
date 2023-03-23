from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import create_app

application = create_app()

#db = SQLAlchemy(application)

if __name__ == '__main__':
    application.run(debug=True)

