import requests
import logging

# Define the database file
DB_FILE = "products.db"

# Set up module-level logger
logger = logging.getLogger(__name__)

def lookup_openfoodfacts(barcode):
    """
    Queries Open Food Facts API and retrieves useful product details.
    
    Args:
        barcode (str): The product barcode to look up
        
    Returns:
        dict: Product information dictionary or None if not found/error
        
    Raises:
        ValueError: If barcode is invalid
    """
    if not barcode or not isinstance(barcode, str):
        logger.error(f"Invalid barcode provided: {barcode}")
        raise ValueError("Invalid barcode format")
        
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    logger.info(f"Querying Open Food Facts API for barcode: {barcode}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Handle HTTP errors
        data = response.json()

        if data.get("status") == 0 or "product" not in data:
            logger.warning(f"Product not found for barcode: {barcode}")
            return None  # Product not found

        product = data["product"]
        logger.info(f"Successfully retrieved data for product: {product.get('product_name', 'Unknown')}")

        # Extract useful information
        product_info = {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Unknown"),
            "allergens": product.get("allergens", "None"),
            "calories": product.get("nutriments", {}).get("energy-kcal", 0),
            "fat": product.get("nutriments", {}).get("fat", 0),
            "saturated_fat": product.get("nutriments", {}).get("saturated-fat", 0),
            "carbohydrates": product.get("nutriments", {}).get("carbohydrates", 0),
            "sugars": product.get("nutriments", {}).get("sugars", 0),
            "proteins": product.get("nutriments", {}).get("proteins", 0),
            "sodium": product.get("nutriments", {}).get("sodium", 0),
            "nutriscore": product.get("nutriscore_grade", "Unknown"),
            "ecoscore": product.get("ecoscore_grade", "Unknown"),
            "image_url": product.get("image_url", "Unknown"),
            "store": product.get("stores", "Unknown")
        }

        return product_info

    except requests.exceptions.Timeout:
        logger.error(f"Timeout when fetching product data for barcode: {barcode}")
        return None
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}, Status code: {e.response.status_code}")
        return None
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error when fetching product data for barcode: {barcode}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data: {e}")
        return None
    except ValueError as e:
        logger.error(f"Error parsing JSON response: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error when processing barcode {barcode}: {e}")
        return None