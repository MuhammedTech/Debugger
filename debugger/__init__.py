from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_dance.contrib.github import make_github_blueprint,github
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = '/Users/a10.12/PycharmProjects/QuestionAnswer/debugger/static/files'
github_blueprint = make_github_blueprint(client_id='93e10ada75a2ab76de95',
                                         client_secret='675fdb312b37057461ff55a6be96002d9afec41a')
app.register_blueprint(github_blueprint,url_prefix='/github_login')

db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

from debugger import routes

#export FLASK_APP=run.py
#flask db u