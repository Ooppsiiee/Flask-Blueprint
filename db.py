from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserData.sqlite3'
db = SQLAlchemy(app)

class DataUser(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    unique_key = db.Column(db.String(100))



if __name__ == "__main__":
    app.run()