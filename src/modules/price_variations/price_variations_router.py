from time import time
from flask import Blueprint, make_response
from src.server.helpers.default_response import default_response
from src.modules.price_variations.repositories.save_price_variation_of_the_day_repository import save_price_variation_of_the_day

price_variations_router = Blueprint('price_variations_router', __name__, url_prefix='/price_variation')


@price_variations_router.route('/')
def index():
    return 'hello'


@price_variations_router.route('/save_all', methods=['GET'])
def save_all_products_price_variations():
    start = time()
    try:
        save_price_variation_of_the_day()

        return make_response(
            default_response('Saved', 201, start)
        )
    except Exception:
        raise
