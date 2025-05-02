from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

# Set up your MySQL connection string
DATABASE_URL = "mysql+mysqlconnector://root:<YOUR_PASSWORD>@localhost/<YOUR_DATABASE_NAME>"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass
