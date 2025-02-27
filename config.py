import os
import logging

class Config:
    """Configuration settings for the Flask application."""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_FILE = os.path.join(BASE_DIR, 'products.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    
    # Logging configuration
    LOG_LEVEL = getattr(logging, os.environ.get('LOG_LEVEL', 'INFO'))
    ROUTES_LOG_LEVEL = getattr(logging, os.environ.get('ROUTES_LOG_LEVEL', 'DEBUG'))
    FOOD_DATA_LOG_LEVEL = getattr(logging, os.environ.get('FOOD_DATA_LOG_LEVEL', 'INFO'))
    DB_LOG_LEVEL = getattr(logging, os.environ.get('DB_LOG_LEVEL', 'WARNING'))