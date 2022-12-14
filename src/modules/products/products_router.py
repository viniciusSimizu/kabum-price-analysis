from time import time
from flask import Blueprint, make_response

from src.modules.products.services.product_find_and_save_service import product_find_and_save_service
from src.server.helpers.default_response import default_response
from src.server.firebase.initialize_server import db

# Services
from src.modules.products.services.list_product_service import list_product_service
from src.modules.products.services.find_product_by_id_service import find_product_by_id_service

products_router = Blueprint('products_router', __name__, url_prefix='/product')


@products_router.route('/', methods=['GET'])
def list_products():
    start = time()
    try:
        products = list_product_service()

        return make_response(
            default_response(products, 200, start)
        )
    except Exception:
        raise


@products_router.route('/<int:product_id>', methods=['POST'])
def find_and_save(product_id):
    start = time()
    try:
        product = product_find_and_save_service(str(product_id))

        return make_response(
            default_response(product, 200, start)
        )
    except Exception:
        raise
