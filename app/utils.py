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

def format_allergens(allergen_string):
    """
    Format allergens string by removing 'en:' prefixes and adding spaces after commas.
    Example: 'en:gluten,en:peanuts' -> 'Gluten, Peanuts'
    """
    if allergen_string == "None" or not allergen_string:
        return "None"
        
    # Split by comma and clean each allergen
    allergens = allergen_string.split(',')
    cleaned_allergens = []
    
    for allergen in allergens:
        # Remove 'en:' prefix and any language code prefix
        if ':' in allergen:
            allergen = allergen.split(':')[-1]
        # Capitalize and add to list
        cleaned_allergens.append(allergen.strip().capitalize())
    
    # Join with comma and space
    return ', '.join(cleaned_allergens)

