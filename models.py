from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String, unique=True, nullable=False)
    quantity = db.Column(db.Numeric, unique=False, nullable=False)
    creation_date = db.Column(db.String, unique=False, nullable=False)
    updates = db.Column(db.JSON, unique=False, nullable=False)

    def __init__(self, stock_name, quantity):
        self.stock_name = stock_name
        self.quantity = quantity
        self.creation_date = datetime.now()
        self.updates = []


db.create_all()
