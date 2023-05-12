from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os

# Initialize SQLAlchemy
db = SQLAlchemy()
DB_NAME = "appdata.db"

# Create Flask app and configure it
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

# Set the upload folder for the app
app.config['UPLOAD_FOLDER'] = 'codebase/website/static'

# Import and register blueprints for different sections of the app
from .views import views
from .auth import auth
from .chats import chats, chats_BP


app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(chats_BP, url_prefix='/')

#Create the database tables if they don't exist
from .models import User, Note
   
with app.app_context():
        db.create_all()

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Define the user loader function for the LoginManager
@login_manager.user_loader
def load_user(id):
 return User.query.get(int(id))

# Function to create the database if it doesn't exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
