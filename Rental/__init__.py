from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__) 
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pr0x.sqlite3'
db.init_app(app)
from .models import DataUser
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


