from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_order_db,
    get_product_db,
)

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

from app.services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

#this
@router.post("/", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    order_db: Session = Depends(get_order_db),
    product_db: Session = Depends(get_product_db),
):
    return OrderService.create_order(
        order_db,
        product_db,
        order,
    )


@router.get("/", response_model=list[OrderResponse])
def get_orders(
    db: Session = Depends(get_order_db),
):
    return OrderService.get_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_order_db),
):
    return OrderService.get_order(
        db,
        order_id,
    )


@router.get("/user/{user_id}", response_model=list[OrderResponse])
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_order_db),
):
    return OrderService.get_user_orders(
        db,
        user_id,
    )


@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_order_db),
):
    return OrderService.delete_order(
        db,
        order_id,
    )