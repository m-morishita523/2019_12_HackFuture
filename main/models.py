from main import db
from flask_sqlalchemy import SQLAlchemy

class Entry(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return "<Entry id={} title={!r}>".format(self.id, self.title)

class EnglishArchive(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.Text)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<Entry id={} shopname={!r}>".format(self.id, self.shopname)

def init():
    db.create_all()