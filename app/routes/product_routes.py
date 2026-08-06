from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.dependencies import get_product_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_product_db),
):
    return ProductService.create_product(
        db,
        product,
    )


@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_product_db),
):
    return ProductService.get_products(db)


# ⭐ NEW SEARCH ENDPOINT
@router.get("/search", response_model=list[ProductResponse])
def search_products(
    keyword: str | None = Query(default=None),
    min_price: float | None = Query(default=None),
    max_price: float | None = Query(default=None),
    db: Session = Depends(get_product_db),
):
    return ProductService.search_products(
        db=db,
        keyword=keyword,
        min_price=min_price,
        max_price=max_price,
    )


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_product_db),
):
    return ProductService.get_product(
        db,
        product_id,
    )


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_product_db),
):
    return ProductService.update_product(
        db,
        product_id,
        product,
    )


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_product_db),
):
    return ProductService.delete_product(
        db,
        product_id,
    )