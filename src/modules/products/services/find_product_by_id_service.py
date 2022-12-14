from src.modules.products.repositories.find_product_by_id_repository import find_product_by_id_repository


def find_product_by_id_service(product_id: str):
    product = find_product_by_id_repository(product_id)

    return product
