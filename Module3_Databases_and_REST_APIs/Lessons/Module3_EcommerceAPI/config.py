import os

# Update this to match your MySQL login
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "your_mysql_password")

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{DB_PASSWORD}@localhost/ecommerce_api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
