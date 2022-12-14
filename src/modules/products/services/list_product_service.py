from src.modules.products.repositories.list_product_repository import list_product_repository


def list_product_service():
    products = list_product_repository()

    return products
