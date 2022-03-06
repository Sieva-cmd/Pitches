from . import db
from datetime import datetime

class Pitch(db.Model):
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text())
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True)
   


    def __repr__(self):
        return f'Pitch {self.title}'