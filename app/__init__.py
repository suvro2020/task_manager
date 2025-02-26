from flask import Flask
from .database import init_db
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'rootpassword'
    app.config['MYSQL_DB'] = 'task_manager'

    # Initialize the database
    init_db(app)
   

    # Register the routes
    app.register_blueprint(main_bp)

    return app
