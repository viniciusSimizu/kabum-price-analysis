from src.modules.products.services.find_product_by_id_service import find_product_by_id_service
from src.modules.products.services.watch_product_service import watch_product_service


def product_find_and_save_service(product_id: str):
    saved_product = find_product_by_id_service(product_id)

    if not saved_product:
        watch_product_service(product_id)
        return find_product_by_id_service(product_id)
    else:
        return saved_product
