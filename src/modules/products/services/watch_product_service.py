from src.modules.price_variations.helpers.factories import product_factory
from src.modules.products.helpers.get_product_infos import get_product_infos_by_id
from src.server.firebase.initialize_server import db


def watch_product_service(product_id: str):
    product_infos = get_product_infos_by_id(product_id)
    firebase_save_product(product_infos)


def firebase_save_product(response: dict) -> None:
    produto = product_factory(response)
    del produto['codigo']

    db.collection(u'Produtos').document(str(response['codigo'])).set(produto)
