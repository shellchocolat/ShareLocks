# main.py

from flask import Blueprint, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from . import locks

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@cross_origin()
def home():
    brands = list_brands()
    return render_template('index.html', brands=brands)

def list_brands():
    r = locks["locks"]
    brands = []
    for brand in r:
        brands.append(brand)
    return brands 

@main.route('/', methods=['POST'])
@cross_origin()
def get_lock():
    brand = request.form.get('brand')
    brands = list_brands()
    models = locks["locks"][brand]
    return render_template('index.html', brands=brands, models=models)
