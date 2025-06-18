from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()  
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
