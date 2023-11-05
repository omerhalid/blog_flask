from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(50), nullable=False)
    
class BuyStock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=True)