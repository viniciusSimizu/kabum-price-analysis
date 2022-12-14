from datetime import date, datetime
from google.cloud.firestore import ArrayUnion
from src.modules.price_variations.helpers.factories import price_variation_factory
from src.modules.products.helpers.get_product_infos import get_product_infos_by_id
from src.modules.products.repositories.list_product_repository import list_product_repository
from src.server.firebase.initialize_server import db


def save_price_variation_of_the_day():
    with open('saves_logs.txt', 'a') as file:
        # Write the start time of execution
        date_time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')
        file.write(f"{date_time:-^80}\n")

        for product in list_product_repository():
            # Verify if the price has already been saved
            if product['variacao_precos'][-1]['created_at'] != str(date.today()):
                try:
                    product_infos = get_product_infos_by_id(product.id)
                    firebase_save_price(product_infos)

                    file.write(f"[{product.id}]: Product Price saved - {product['nome']}\n")
                except Exception as err:
                    file.write(f"[{product.id}]: Error - {err} - {product['nome']}\n")

        # Finish execution
        file.write(f"{'':-^80}\n\n")
        file.close()


def firebase_save_price(response: dict) -> None:
    variacao_preco = price_variation_factory(response)

    db.collection(u'Produtos').document(str(response['codigo'])).update(
        dict(variacao_precos=ArrayUnion([variacao_preco])))
