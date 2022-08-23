# __init__.py
 
from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os

current_dir = os.getcwd()
with open("./app/locks.json", "r") as fp:
    locks = fp.read()
locks = json.loads(locks)

def create_app():
    app = Flask(__name__, 
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates')

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

