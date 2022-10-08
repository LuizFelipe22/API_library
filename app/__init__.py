__version__ = '1.0.1'

from flask import Flask


app = Flask(__name__)


from app.all_routes import *
