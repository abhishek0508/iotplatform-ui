from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# define what our database user looks like.
class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column('application_id', db.Integer, primary_key=True)
    filepath = db.Column('filepath', db.String(60))
    parent_id = Column(Integer, ForeignKey('User.id'))

    def __init__(self, filepath):
        self.filepath = filepath

