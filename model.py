from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    pages = db.Column(db.Integer)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
