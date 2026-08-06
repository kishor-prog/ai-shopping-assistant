from app.database.product_db import SessionLocal as ProductSessionLocal
from app.database.order_db import SessionLocal as OrderSessionLocal

#this function is used to get the product database session
def get_product_db():
    db = ProductSessionLocal()
    try:
        yield db
    finally:
        db.close()

#this function is used to get the order database sessionSSSSS
def get_order_db():
    db = OrderSessionLocal()
    try:
        yield db
    finally:
        db.close()