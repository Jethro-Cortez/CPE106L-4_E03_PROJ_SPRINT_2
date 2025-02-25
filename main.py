from flask import Flask
from config import Config
from lms_app import create_app

app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=True)
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}")