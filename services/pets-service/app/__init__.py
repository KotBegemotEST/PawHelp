from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from .routes import main

load_dotenv()
db = SQLAlchemy()  

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
