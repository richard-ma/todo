import datetime
from src.models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    status = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    finish_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
