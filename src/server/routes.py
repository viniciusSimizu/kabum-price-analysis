from flask import Flask
from src.modules.price_variations.price_variations_router import price_variations_router
from src.modules.products.products_router import products_router


def create_routes(app: Flask):
    app.register_blueprint(price_variations_router)
    app.register_blueprint(products_router)

    return app
