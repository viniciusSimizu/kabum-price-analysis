import re
from datetime import date


def price_variation_factory(response):
    return dict(
        produto_id=response['codigo'],
        preco_original=response['preco'],
        preco_desconto=response['preco_desconto'],
        preco_prime=response['preco_prime'],
        preco_desconto_prime=response['preco_desconto_prime'],
        quantidade=response['oferta']['quantidade'] if response['oferta'] is not None else None,
        created_at=str(date.today())
    )


def product_factory(response):
    # Save Categories
    menus = response['menus']

    # Create Manufacturer Instance
    fabricante = response['fabricante']
    fabricante = dict(
        codigo=fabricante['codigo'],
        nome=fabricante['nome']
    )

    # Create Department Instance
    departamento = menus[0]
    departamento = dict(
        codigo=departamento['codigo'],
        amigavel=departamento['amigavel'],
        nome=departamento['nome'],
    )

    # Create Category Instance
    categoria = menus[1]
    categoria = dict(
        codigo=categoria['codigo'],
        amigavel=categoria['amigavel'],
        nome=categoria['nome'],
        departamento=departamento
    )

    # Create SubCategory Instance
    subcategoria = menus[2]
    subcategoria = dict(
        codigo=subcategoria['codigo'],
        amigavel=subcategoria['amigavel'],
        nome=subcategoria['nome'],
        categoria=categoria
    )

    first_pattern = r"https://images(\d+)."
    second_pattern = r"/fotos/(\d+[\S]+).jpg"
    # Create Product Instance
    produto_dict = dict(
        nome=response['nome'],
        codigo=response['codigo'],
        link=response['link_descricao'],
        fabricante=fabricante,
        sub_categoria=subcategoria,
        variacao_precos=[price_variation_factory(response)],
        fotos=[
            f"{re.search(first_pattern, pic_url).group(1)} {re.search(second_pattern, pic_url).group(1)}"
            for pic_url in response['fotos']
        ]
    )

    return produto_dict
