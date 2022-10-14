__version__ = '1.0.2'

from flask import Flask

from app.database.db_session import create_tables


app = Flask(__name__)

db = create_tables()


from app.all_routes import *
