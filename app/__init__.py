from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
from config import Config

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def reg_bluprint(application):
    from .main import main as main_blueprint
    application.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    application.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    application.register_blueprint(auth_blueprint, url_prefix='/auth')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    CSRFProtect(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    reg_bluprint(app)

    return app
