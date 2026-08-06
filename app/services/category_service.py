from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate

#this class is used to handle the business logic for category operations create, get, update, delete
class CategoryService:

    @staticmethod
    def create_category(
        db: Session,
        category: CategoryCreate
    ):
        existing = CategoryRepository.get_by_name(
            db,
            category.name
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Category '{category.name}' already exists."
            )

        return CategoryRepository.create(
            db,
            category.name,
            category.description,
        )

    @staticmethod
    def get_categories(db: Session):
        return CategoryRepository.get_all(db)

    @staticmethod
    def get_category(
        db: Session,
        category_id: int
    ):
        category = CategoryRepository.get_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        return category

    @staticmethod
    def update_category(
        db: Session,
        category_id: int,
        data: CategoryUpdate
    ):
        category = CategoryRepository.get_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        existing = CategoryRepository.get_by_name(
            db,
            data.name
        )

        if existing and existing.id != category_id:
            raise HTTPException(
                status_code=400,
                detail=f"Category '{data.name}' already exists."
            )

        return CategoryRepository.update(
            db,
            category,
            data
        )

    @staticmethod
    def delete_category(
        db: Session,
        category_id: int
    ):
        category = CategoryRepository.get_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        CategoryRepository.delete(
            db,
            category
        )

        return {
            "message": "Category deleted successfully"
        }