from decimal import Decimal
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate

# This class is used to interact with the Product table in the database
class ProductRepository:

    @staticmethod
    def create(
        db: Session,
        product: ProductCreate
    ):
        db_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            sku=product.sku,
            category_id=product.category_id
        )

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_by_id(
        db: Session,
        product_id: int
    ):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    @staticmethod
    def get_by_sku(
        db: Session,
        sku: str
    ):
        return (
            db.query(Product)
            .filter(Product.sku == sku)
            .first()
        )

    @staticmethod
    def search(
        db: Session,
        keyword: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
    ):
        query = (
            db.query(Product)
            .join(Category, Product.category_id == Category.id)
        )

        if min_price is not None:
            query = query.filter(Product.price >= Decimal(str(min_price)))

        if max_price is not None:
            query = query.filter(Product.price <= Decimal(str(max_price)))

        if keyword:
            raw_keyword = keyword.strip()
            keyword_lower = raw_keyword.lower()

            # ------------------------------------------------
            # 1. Exact product name
            # ------------------------------------------------
            exact_products = (
                query.filter(
                    Product.name.ilike(raw_keyword)
                ).all()
            )

            if exact_products:
                return exact_products

            # Remove plural 's'
            words = []
            for word in keyword_lower.split():
                if word.endswith("s") and len(word) > 3:
                    word = word[:-1]
                words.append(word)

            normalized_keyword = " ".join(words)

            # ------------------------------------------------
            # 2. Full phrase match
            # ------------------------------------------------
            phrase_products = (
                query.filter(
                    Product.name.ilike(f"%{raw_keyword}%")
                ).all()
            )

            if not phrase_products and normalized_keyword != keyword_lower:
                phrase_products = (
                    query.filter(
                        Product.name.ilike(f"%{normalized_keyword}%")
                    ).all()
                )

            if phrase_products:
                return phrase_products

            # ------------------------------------------------
            # 3. Search each word individually
            # ------------------------------------------------
            if words:
                filters = []
                for word in words:
                    filters.extend([
                        Product.name.ilike(f"%{word}%"),
                        Product.description.ilike(f"%{word}%"),
                        Category.name.ilike(f"%{word}%"),
                    ])

                query = query.filter(or_(*filters))

        return query.all()

    @staticmethod
    def update(
        db: Session,
        db_product: Product,
        product: ProductCreate
    ):
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.sku = product.sku
        db_product.category_id = product.category_id

        db.commit()
        db.refresh(db_product)

        return db_product

    @staticmethod
    def delete(
        db: Session,
        db_product: Product
    ):
        db.delete(db_product)
        db.commit()