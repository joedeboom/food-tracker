from sqlalchemy import Column, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine for our SQLite database
engine = create_engine("sqlite:///products.db", echo=False)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    barcode = Column(String, primary_key=True, index=True)
    product_name = Column(String)
    brand = Column(String)
    ingredients = Column(String)
    allergens = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    saturated_fat = Column(Float)
    carbohydrates = Column(Float)
    sugars = Column(Float)
    proteins = Column(Float)
    sodium = Column(Float)
    nutriscore = Column(String)
    ecoscore = Column(String)
    image_url = Column(String)
    store = Column(String)