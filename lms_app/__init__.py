from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# ✅ Initialize extensions globally (no imports yet)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ✅ Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # ⏰ Move imports INSIDE create_app (avoids circular imports)
    with app.app_context():
        from lms_app import models
        from lms_app.routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
