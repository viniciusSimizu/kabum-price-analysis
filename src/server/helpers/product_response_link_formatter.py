def links_format(product: dict):
    product['fotos'] = [
        f"https://images{link.split(' ')[0]}.kabum.com.br/produtos/fotos/{link.split(' ')[1]}.jpg"
        for link in product['fotos']
    ]

    return product