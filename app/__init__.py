from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # vista a redirigir si no está logueado

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # IMPORTACIONES Y REGISTRO DE BLUEPRINTS
    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # CARGADOR DE USUARIO
    from .models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(user_id)

    return app
