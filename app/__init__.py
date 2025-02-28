from flask import Flask
from app.database import create_database
import logging
import os

def configure_logging(app):
    """Configure logging for the application."""
    log_level = app.config.get('LOG_LEVEL', logging.INFO)
    
    # Configure the root logger
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    
    # Configure module-specific log levels
    logging.getLogger('werkzeug').setLevel(logging.WARNING)  # Reduce Flask web server logs
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    
    # Set app-specific module log levels
    logging.getLogger('app.routes').setLevel(app.config.get('ROUTES_LOG_LEVEL', log_level))
    logging.getLogger('app.food_data').setLevel(app.config.get('FOOD_DATA_LOG_LEVEL', log_level))
    logging.getLogger('app.database').setLevel(app.config.get('DB_LOG_LEVEL', log_level))
    
    app.logger.info(f"Logging configured at level: {logging.getLevelName(log_level)}")



def create_app():
    app = Flask(__name__)
    
    # Add these lines to configure the app with the secret key from config.py
    from config import Config
    app.config.from_object(Config)
    
    # Configure logging
    configure_logging(app)
    
    # Register custom template filters
    from app.utils import format_allergens
    app.jinja_env.filters['format_allergens'] = format_allergens
    
    # Add CSRFProtect
    from flask_wtf.csrf import CSRFProtect
    csrf = CSRFProtect(app)
    
    # Create database and tables
    create_database()
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# Don't call create_app here