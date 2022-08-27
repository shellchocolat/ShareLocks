# main.py

from flask import Blueprint, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from . import locks

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@cross_origin()
def home():
    brands = list_brands()
    num_locks = get_num_locks()
    return render_template('index.html', brands=brands, num_locks=num_locks)

def list_brands():
    brands = {}
    for brand in locks["locks"]:
        brands[brand] = len(locks["locks"][brand])
    return brands 

def get_num_locks():
    num_locks = 0
    for brand in locks["locks"]:
        num_locks += len(locks["locks"][brand])
    return num_locks

@main.route('/', methods=['POST'])
@cross_origin()
def get_lock():
    brand = str(request.form.get('brand'))
    brands = list_brands()
    num_locks = get_num_locks()
    models = locks["locks"][brand]
    return render_template('index.html', brands=brands, num_locks=num_locks, models=models)
