import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key_123')
    ADMIN_SECRET_KEY = os.environ.get('ADMIN_SECRET_KEY', 'admin123')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'library_db.sqlite3')
    SQLALCHEMY_BINDS = {
        'users': 'sqlite:///' + os.path.join(basedir, 'users_db.sqlite3'),
        'feedback': 'sqlite:///' + os.path.join(basedir, 'feedback_db.sqlite3')
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
