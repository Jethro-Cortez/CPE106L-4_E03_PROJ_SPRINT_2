import click
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .book_covers import main as download_covers, get_db_path
from config import Config


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # ✅ Call get_db_path inside app context
    with app.app_context():
        DB_PATH = get_db_path()

    def slugify(text):
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[\s_-]+', '-', text)
        text = re.sub(r'^-+|-+$', '', text)
        return text

    app.jinja_env.filters['slugify'] = slugify

    @app.cli.command("download-covers")
    def download_covers_command():
        try:
            download_covers()
            click.echo("✅ Book covers downloaded successfully!")
        except Exception as e:
            click.echo(f"❌ Error downloading covers: {e}")

    return app
