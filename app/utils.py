def product_tuple_to_dict(product):
    """
    Convert a product object to a dictionary.
    """
    return {
        'barcode': product.barcode,
        'product_name': product.product_name,
        'brand': product.brand,
        'ingredients': product.ingredients,
        'allergens': product.allergens,
        'calories': product.calories,
        'image_url': product.image_url
    }