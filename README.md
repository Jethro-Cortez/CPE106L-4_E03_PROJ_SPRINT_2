# 📚 BookIT

A full-stack Library Management System built with **Flask**, **SQLite**, **SQLAlchemy**, and **Flask-Migrate**. It supports user authentication, role-based access control, book management, transaction tracking, and feedback handling. 

---

## ⚡ Features

- 🔐 **User Authentication & Role-Based Access**
- 📖 **Book Borrowing, Returning, and Inventory Management**
- 💰 **Fine Calculation for Overdue Books**
- 🗨️ **User Feedback & Reviews**
- 🌗 **Dark/Light Mode Toggle**
- 📊 **Admin Dashboard with Analytics**
- 🗄️ **SQLite Database with Flask-Migrate for Easy Migrations**

---

## 🛠️ Prerequisites

- **Python 3.8+**
- **Pip** (Python package installer)
- **SQLite3** (Pre-installed with Python, but confirm with `sqlite3 --version`)

---

## 📥 Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Set Up Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   # OR
   source venv/bin/activate  # For Mac/Linux
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables (Windows CMD):**

   ```cmd
   set FLASK_APP=main.py
   set FLASK_ENV=development
   ```

   _For PowerShell:_

   ```powershell
   $env:FLASK_APP="main.py"
   $env:FLASK_ENV="development"
   ```

---

## 🗄️ Database Setup

1. **Initialize Migrations:**

   ```bash
   flask db init
   ```

2. **Generate Migration Script:**

   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply Migrations:**

   ```bash
   flask db upgrade
   ```

---

## 🚀 Running the Application

Start the Flask development server:

```bash
flask run
```

The app will run at:

```
http://localhost:5000/
```

---

## 👑 **Admin Access**

1. **Register as Admin:**  
   Open the following URL in your browser:

   ```
   http://localhost:5000/adminreg?key=sinigangmix
   ```

2. **Fill in the admin registration form.**  
3. **After registration, log in using your admin credentials.**  
4. **Access the Admin Dashboard:**

   ```
   http://localhost:5000/admin_dashboard
   ```

---

## 📁 Project Structure

```
LMS/
│
├── lms_app/
│   ├── __init__.py         # Flask app factory
│   ├── models.py           # Database models (User, Book, Transaction, Feedback)
│   ├── routes.py           # Flask routes
│   ├── templates/          # Jinja2 templates
│   └── static/             # Static files (CSS, JS, images)
│
├── migrations/             # Database migrations (Flask-Migrate)
├── library_db.sqlite3      # SQLite database
├── main.py                 # Flask app entry point
├── config.py               # App configurations
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

---

## 🧯 Troubleshooting

**💥 `sqlite3` Not Recognized?**  
- Add SQLite to your system PATH or reinstall SQLite.

**💥 Flask Can't Locate App?**  
- Ensure `FLASK_APP=main.py` is set in your environment variables.

**💥 Migration Issues?**  
- Reset migrations:

  ```bash
  rmdir /s /q migrations
  del library_db.sqlite3
  flask db init
  flask db migrate -m "Reset migrations"
  flask db upgrade
  ```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
