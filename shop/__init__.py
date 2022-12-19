from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask_login import LoginManager
from os import path
from dotenv import load_dotenv
import os

db = SQLAlchemy()
DB_NAME = "myshop.db"
login_manager = LoginManager()



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
    
    
    from .models import User
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    assets = Environment(app) # create an Environment instance
    
    bundles = {  # define nested Bundle
  'example_style': Bundle(
            'SCSS/myfirstscss.scss',
            filters='pyscss',
            output='Gen/renderedcss.css',
  )
} 
    assets.register(bundles)
    
    return app



def create_database(app):
    if not path.exists('shop/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')