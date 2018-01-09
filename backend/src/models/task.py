from models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    status = db.Column(db.Boolean)
    create_time = db.Column(db.Datetime)
    finish_time = db.Column(db.Datetime)
