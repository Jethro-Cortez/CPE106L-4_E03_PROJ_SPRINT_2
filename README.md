![logo](static/images/logorepo.png)

---

A full-stack Library Management System built with **Flask**, **SQLite**, **SQLAlchemy**, and **Flask-Migrate**. It supports user authentication, role-based access control, book management, transaction tracking, and feedback handling. 

---

## 🖼️ Walkthrough

### 🏠 **Landing Page**

![Landing Page](static/screenshots/landing_page.png)

---

### 🔐 **Login Page**

![Login Page](static/screenshots/login_page.png)

---

### 📝 **User Registration**

![User Registration](static/screenshots/user_registration.png)

---

### 👤 **User Dashboard**

![User Dashboard](static/screenshots/user_dashboard.png)

---

### 👑 **Admin Registration**

![Admin Registration](static/screenshots/admin_registration.png)

---

### 📖 **Add New Book**

![Book Details](static/screenshots/add_new_book.png)

---

### 📊 **Admin Dashboard**

![Admin Dashboard](static/screenshots/admin_dashboard.png)

![Admin Dashboard 2](static/screenshots/admin_dashboard(2).png)

---

### 🌗 **Dark Mode Toggle**

![light mode](static/screenshots/dark_mode.png) 

![Dark Mode](static/screenshots/dark_mode(2).png)

---

# Problems in this project 

- ❌ Haven't added new books  

- ⚠️ Haven't tested the "Add New Book" feature  

- 😥 very bright light mode

- 🧩 Jenga code

- 🐛 Buggy GUI  

- 🔄 My Python keeps removing itself from the PATH

- 🚫 No global access (Only works on `localhost`)  

- 💣 Very unstable database

- ⏳ Coming soon...


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
   git clone https://github.com/Jethro-Cortez/CPE106L-4_E03_PROJ_SPRINT_2.git
   cd CPE106L-4_E03_PROJ_SPRINT_2
   ```

2. **Set Up Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
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
