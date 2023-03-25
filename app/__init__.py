import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(session_options={
    'expire_on_commit': False
})
migrate = Migrate()
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)
def create_app():
    app = Flask(__name__)
    if 'RDS_HOSTNAME' in os.environ:
      DATABASE = {
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
      }
      database_url = 'mysql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASE
    else:
      database_url = 'sqlite:///' + os.path.join(basedir, 'database.db')

    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = database_url,
        SQLALCHEMY_POOL_RECYCLE = 280,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .tasklist import tasklist_blueprint
    app.register_blueprint(tasklist_blueprint)
    return app
