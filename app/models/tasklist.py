from flask import current_app
from .. import db


class Task(db.Model):
    __tablename__ = 'task_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    def __repr__(self):
        return '<Task: {}>'.format(self.name)
    

    
