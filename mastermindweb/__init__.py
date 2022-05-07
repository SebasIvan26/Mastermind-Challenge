import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

# Retrieve databse_url from Heroku environment
postgres_url = os.getenv('DATABASE_URL', 'None')

############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#########################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



##################################################


from mastermindweb.core.views import core
from mastermindweb.users.views import users
from mastermindweb.error_pages.handlers import error_pages
from mastermindweb.blog_posts.views import blog_posts
from mastermindweb.game.views import game

app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(game)
