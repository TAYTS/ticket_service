""" Testing Configurations """
from datetime import timedelta

# Environment
TESTING = True
PROPAGATE_EXCEPTIONS = True

# SQL
SQLALCHEMY_DATABASE_URI = "mysql://user:testing@127.0.0.1:3306/user_testing"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 299
SQLALCHEMY_POOL_RECYCLE = 20
PREFERRED_URL_SCHEME = "https"

# Log
APP_LOG_FILE = "log/app.log"
APP_LOG_LEVEL = "DEBUG"

# JWT
JWT_SECRET_KEY = "secret-key"
JWT_TOKEN_LOCATION = "cookies"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7300)
JWT_CSRF_METHODS = ["GET", "POST", "PUT", "DELETE"]
JWT_COOKIE_SECURE = False
JWT_COOKIE_DOMAIN = "127.0.0.1"

# MESSAGE API
MESSAGE_API = "http://127.0.0.1:5000/messages/"
