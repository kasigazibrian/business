from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

class Signup(db.Model):
    __tablename__="signup"
    id = db.Column(db.Integer, primary_key= True,nullable=False, autoincrement=True)
    firstname = db.Column( db.VARCHAR(100), nullable=False)
    lastname = db.Column( db.VARCHAR(100),nullable=False)
    username = db.Column( db.VARCHAR(50), unique=True,nullable=False)
    password = db.Column( db.VARCHAR(50),nullable=False)
    phonenumber = db.Column( db.VARCHAR(20))
    email = db.Column( db.VARCHAR(100), unique=True, nullable=False)
    gender = db.Column(db.String(10))

    def __init__(self, firstname, lastname, username, password, phonenumber, email, gender):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
        self.phonenumber=phonenumber
        self.email=email
        self.gender=gender
        #self.id= id


class Login(db.Model):
    __tablename__= 'login'
    id = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    username = db.Column(db.VARCHAR(50), unique=True)
    password = db.Column(db.VARCHAR(50), unique=True)
    business_owner = db.relationship('BusinessRegistration',backref='owner' , lazy='dynamic')

    def __init__(self, username, password):
        #self.id= id
        self.username = username
        self.password = password
class BusinessRegistration(db.Model):
    business_id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    business_owner_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    businessname = db.Column(db.VARCHAR(100), nullable=False)
    business_street_address = db.Column(db.VARCHAR(200), nullable=False)
    business_city = db.Column(db.VARCHAR(30),nullable=False)
    business_country = db.Column(db.VARCHAR(30),nullable=False)
    contact_number = db.Column(db.VARCHAR(15), nullable=False)
    email = db.Column(db.VARCHAR(50),nullable=False)
    firstname = db.Column(db.VARCHAR(20), nullable=False)
    lastname = db.Column(db.VARCHAR(20), nullable=False)
    nominalcapital = db.Column(db.FLOAT, nullable=False)
    business_cateogory = db.Column(db.VARCHAR(150), nullable=False)

    def __init__(self, businessname, business_street_address, business_city, business_country, contact_number, email, firstname, lastname, nominalcapital,business_category, business_owner_id):
        self.businessname=businessname
        self.business_street_address = business_street_address
        self.business_owner_id = business_owner_id
        self.business_city = business_city
        self.business_country = business_country
        self.contact_number = contact_number
        self.email=email
        self.firstname = firstname
        self.lastname = lastname
        self.nominalcapital = nominalcapital
        self.business_cateogory = business_category
