from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_product_db
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "/",
    response_model=CategoryResponse,
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_product_db),
):
    return CategoryService.create_category(
        db,
        category,
    )


@router.get(
    "/",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_product_db),
):
    return CategoryService.get_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_category(
    category_id: int,
    db: Session = Depends(get_product_db),
):
    return CategoryService.get_category(
        db,
        category_id,
    )


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_product_db),
):
    return CategoryService.update_category(
        db,
        category_id,
        category,
    )


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_product_db),
):
    return CategoryService.delete_category(
        db,
        category_id,
    )