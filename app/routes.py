from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.food_data import lookup_openfoodfacts
from app.database import save_product, get_all_products
from app.utils import product_tuple_to_dict
from app.models import Product, SessionLocal
import logging

# Just get the logger for this module
logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    logger.debug("Loading index page")
    try:
        products = get_all_products()
        # Convert tuple rows to dictionaries using the helper function
        product_list = [product_tuple_to_dict(product) for product in products]
        return render_template('index.html', products=product_list)
    except Exception as e:
        logger.exception("Error loading products: %s", str(e))
        flash("An error occurred while loading products", "error")
        return render_template('index.html', products=[])

@main.route('/add_product', methods=['GET'])
def add_product():
    logger.debug("Add product route called with method: %s", request.method)
    
    # Get barcode from query parameter
    barcode = request.args.get('barcode')
    
    if not barcode:
        flash("Please provide a valid barcode", "warning")
        logger.warning("Add product called without a barcode")
        return redirect(url_for('main.index'))
        
    logger.debug("Looking up barcode: %s", barcode)
    
    try:
        product_info = lookup_openfoodfacts(barcode)
        
        if product_info:
            logger.debug("Product found, saving to database")
            save_product(product_info)
            flash(f"Product '{product_info['product_name']}' successfully added", "success")
        else:
            logger.warning(f"No product found for barcode: {barcode}")
            flash(f"No product found for barcode: {barcode}", "warning")
    except ValueError as e:
        logger.error(f"Invalid barcode format: {e}")
        flash(f"Invalid barcode format: {str(e)}", "error")
    except Exception as e:
        logger.exception(f"Error processing barcode {barcode}: {e}")
        flash("An error occurred while processing the product", "error")
    
    return redirect(url_for('main.index'))

@main.route('/product/<barcode>', methods=['GET'])
def product_detail(barcode):
    logger.debug(f"Loading detail page for product barcode: {barcode}")
    try:
        session = SessionLocal()
        product = session.query(Product).filter(Product.barcode == barcode).first()
        session.close()
        
        if not product:
            logger.warning(f"Product not found for barcode: {barcode}")
            flash("Product not found", "error")
            return redirect(url_for('main.index'))
            
        return render_template('product_detail.html', product=product)
    except Exception as e:
        logger.exception(f"Error loading product detail: {str(e)}")
        flash("An error occurred while loading the product", "error")
        return render_template('error.html', error="Failed to load product details"), 500


@main.route('/delete_product/<barcode>', methods=['POST'])
def delete_product(barcode):
    logger.debug(f"Deleting product with barcode: {barcode}")
    try:
        from app.database import delete_product as db_delete_product
        
        if db_delete_product(barcode):
            logger.info(f"Successfully deleted product with barcode: {barcode}")
            flash("Product successfully deleted", "success")
        else:
            logger.warning(f"Product not found for deletion: {barcode}")
            flash("Product not found", "warning")
            
    except Exception as e:
        logger.exception(f"Error deleting product: {str(e)}")
        flash("An error occurred while deleting the product", "error")
        
    return redirect(url_for('main.index'))




# Add application-wide error handlers
@main.app_errorhandler(404)
def page_not_found(e):
    logger.warning(f"Page not found: {request.path}")
    return render_template('error.html', error="Page not found"), 404

@main.app_errorhandler(500)
def server_error(e):
    logger.error(f"Server error: {str(e)}")
    return render_template('error.html', error="Internal server error"), 500