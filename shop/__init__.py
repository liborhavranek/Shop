from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from dotenv import load_dotenv
import os

db = SQLAlchemy()
DB_NAME = "myshop.db"




def configure():
    load_dotenv()

def create_app():
    app = Flask(__name__)
    configure()
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')