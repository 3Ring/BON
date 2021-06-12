from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Setting up MYSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/BON'


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'is it secret?'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///liteBON.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .classes import Users

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Users.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .BONapp import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app