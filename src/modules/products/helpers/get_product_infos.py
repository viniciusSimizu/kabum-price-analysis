from src.server.helpers.default_get_request import default_get_request


def get_product_infos_by_id(product_id: str):
    response = default_get_request(f"descricao/v1/descricao/produto/{product_id}")
    if response.status_code == 404:
        raise Exception('Invalid Product ID')

    return response.json()
