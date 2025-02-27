from sqlalchemy.orm import Session
from app.models import Base, engine, Product, SessionLocal

def create_database():
    """Creates database tables using SQLAlchemy."""
    Base.metadata.create_all(bind=engine)

def save_product(product_info):
    """Inserts or updates product details in the database using SQLAlchemy."""
    session: Session = SessionLocal()
    try:
        # Check if the product already exists
        existing_product = session.query(Product).filter(Product.barcode == product_info["barcode"]).first()
        if existing_product:
            # Update each field for the existing product
            for key, value in product_info.items():
                setattr(existing_product, key, value)
        else:
            # Create and add a new product record
            new_product = Product(**product_info)
            session.add(new_product)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_products():
    """Fetch all products from the database using SQLAlchemy."""
    session: Session = SessionLocal()
    try:
        products = session.query(Product).all()
        return products
    finally:
        session.close()

def delete_product(barcode):
    """Delete a product from the database using SQLAlchemy."""
    session = SessionLocal()
    try:
        product = session.query(Product).filter(Product.barcode == barcode).first()
        if product:
            session.delete(product)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()