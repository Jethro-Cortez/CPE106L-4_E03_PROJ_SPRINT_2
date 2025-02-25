from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from lms_app import db, login_manager
from slugify import slugify

# -------------------------
# 📚 User Model
# -------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), default='user')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)

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
# 📗 Book Model
# -------------------------
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # 📖 Initialize Book
    def __init__(self, title, author, category, description):
        self.title = title
        self.slug = self.generate_unique_slug(title)
        self.author = author
        self.category = category
        self.description = description

    def generate_unique_slug(self, title):
        base_slug = slugify(title)
        slug = base_slug
        counter = 1

        while Book.query.filter_by(slug=slug).first():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

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
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    book = db.relationship('Book', backref='feedbacks')