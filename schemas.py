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
    
class User(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    
class ContactWhoSendEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_sent_email = db.Column(db.Boolean, nullable=False)