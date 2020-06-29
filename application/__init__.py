from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.config import Config
from flask_login import LoginManager




app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from application import routes