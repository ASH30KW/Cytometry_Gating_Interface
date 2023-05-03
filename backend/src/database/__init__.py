from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the db object first, similar as with the app object in app.py
db = SQLAlchemy(app)

# Needed to initialize/migrate the database
# https://flask-migrate.readthedocs.io/en/latest/
migrate = Migrate(app, db) 

from . import todo

TodoDAO = todo.TodoDAO(db.session)
