from app import create_app, db
from flask_migrate import Migrate
import logging

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
    except Exception as e:
        logging.error(f"Error starting the application: {e}")