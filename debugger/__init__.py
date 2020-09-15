from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from debugger.config import Config




db = SQLAlchemy()

migrate = Migrate(db)
manager = Manager()

manager.add_command('db',MigrateCommand)

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app)
    #manager.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    from debugger.users.routes import users
    from debugger.projects.routes import projects
    from debugger.tickets.routes import tickets
    from debugger.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(tickets)
    app.register_blueprint(main)

    return app
