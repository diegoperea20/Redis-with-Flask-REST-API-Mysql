from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_redis import FlaskRedis  # Importa FlaskRedis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@localhost:3306/flaskmysql'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost:5432/flaskpostgresql'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#                          redis://[:password]@host:port/db
app.config['REDIS_URL'] = 'redis://localhost:6379/0'  # Configura la URL de Redis

db = SQLAlchemy(app)
ma = Marshmallow(app)
redis_client = FlaskRedis(app)  # Inicializa FlaskRedis

from routes import *
from models import Task

with app.app_context():
    db.create_all()
