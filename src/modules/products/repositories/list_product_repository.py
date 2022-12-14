from src.server.firebase.initialize_server import db
from src.server.helpers.product_response_link_formatter import links_format


def list_product_repository():
    try:
        products = [dict(
            **links_format(product.to_dict()),
            codigo=product.id
        ) for product in db.collection(u'Produtos').get()]
        return products
    except Exception as err:
        raise err
