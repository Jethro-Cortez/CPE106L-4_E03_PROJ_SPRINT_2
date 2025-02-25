from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from lms_app import db, login_manager

# -------------------------
# 📚 User Model
# -------------------------

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), default='user')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -------------------------
# 📖 UserInfo Model
# -------------------------
class UserInfo(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    birthdate = db.Column(db.Date)
    occupation = db.Column(db.String(64))

# -------------------------
# 📗 Book Model
# -------------------------
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    category = db.Column(db.String(50))
    cover_path = db.Column(db.String(200))  # Path to cover image

    # Relationships
    transactions = db.relationship('Transaction', backref='book', lazy=True)

# -------------------------
# 📊 Transaction Model
# -------------------------
class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='Borrowed')  # Borrowed/Returned/Overdue
    fine_amount = db.Column(db.Float, default=0.0)  # 💰 Fine for overdue

# -------------------------
# 💬 Feedback Model
# -------------------------
class Feedback(db.Model):
    __bind_key__ = 'feedback'
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    admin_response = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
