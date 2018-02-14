from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config.from_pyfile('../config.py')
# app.secret_key = os.urandom(12)
db = SQLAlchemy(app)
from app import views

