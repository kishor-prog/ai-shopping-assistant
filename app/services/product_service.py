from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.product import ProductCreate

#this class is used to handle the business logic for product operations create, get, update, delete
class ProductService:

    @staticmethod
    def create_product(
        db: Session,
        product: ProductCreate
    ):
        # Check whether the category exists
        category = CategoryRepository.get_by_id(
            db,
            product.category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found."
            )

        # Check for duplicate SKU
        existing = ProductRepository.get_by_sku(
            db,
            product.sku
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"SKU '{product.sku}' already exists."
            )

        return ProductRepository.create(
            db,
            product
        )

    @staticmethod
    def get_products(db: Session):
        return ProductRepository.get_all(db)

    @staticmethod
    def get_product(
        db: Session,
        product_id: int
    ):
        product = ProductRepository.get_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        return product

    @staticmethod
    def search_products(
        db: Session,
        keyword: str = None,
        min_price: float = None,
        max_price: float = None,
    ):
        products = ProductRepository.search(
            db=db,
            keyword=keyword,
            min_price=min_price,
            max_price=max_price,
        )

        return products

    @staticmethod
    def update_product(
        db: Session,
        product_id: int,
        data: ProductCreate
    ):
        product = ProductRepository.get_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        # Check category exists
        category = CategoryRepository.get_by_id(
            db,
            data.category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found."
            )

        # Check SKU uniqueness
        existing = ProductRepository.get_by_sku(
            db,
            data.sku
        )

        if existing and existing.id != product_id:
            raise HTTPException(
                status_code=400,
                detail=f"SKU '{data.sku}' already exists."
            )

        return ProductRepository.update(
            db,
            product,
            data
        )

    @staticmethod
    def delete_product(
        db: Session,
        product_id: int
    ):
        product = ProductRepository.get_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        ProductRepository.delete(
            db,
            product
        )

        return {
            "message": "Product deleted successfully"
        }