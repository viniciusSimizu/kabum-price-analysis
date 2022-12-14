from src.server.firebase.initialize_server import db
from src.server.helpers.product_response_link_formatter import links_format


def find_product_by_id_repository(product_id: str):
    try:
        product = db.collection(u'Produtos').document(product_id).get()
        product_dict = links_format(product.to_dict())

        return dict(
            **product_dict,
            codigo=product.id
        )
    except Exception as err:
        raise err
