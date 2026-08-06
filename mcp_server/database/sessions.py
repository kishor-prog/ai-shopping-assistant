from app.database.product_db import SessionLocal as ProductSessionLocal
from app.database.order_db import SessionLocal as OrderSessionLocal

#this function is used to get the product database session
def get_product_db():
    return ProductSessionLocal()

#this function is used to get the order database session
def get_order_db():
    return OrderSessionLocal()