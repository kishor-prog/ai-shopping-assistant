from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.order import OrderCreate

#this class is used to handle the business logic for order operations create, get, update, delete
class OrderService:

    @staticmethod
    def create_order(
        order_db: Session,
        product_db: Session,
        order: OrderCreate,
    ):
        # Check User Exists (Order Database)
        user = UserRepository.get_by_id(
            order_db,
            order.user_id,
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        # Check Product Exists (Product Database)
        product = ProductRepository.get_by_id(
            product_db,
            order.product_id,
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        # Validate Quantity
        if order.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than zero."
            )

        # Create Order (Order Database)
        return OrderRepository.create(
            order_db,
            order,
        )

    @staticmethod
    def get_orders(
        db: Session,
    ):
        return OrderRepository.get_all(db)

    @staticmethod
    def get_order(
        db: Session,
        order_id: int,
    ):
        order = OrderRepository.get_by_id(
            db,
            order_id,
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found."
            )

        return order

    @staticmethod
    def get_user_orders(
        db: Session,
        user_id: int,
    ):
        return OrderRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    def delete_order(
        db: Session,
        order_id: int,
    ):
        order = OrderRepository.get_by_id(
            db,
            order_id,
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found."
            )

        OrderRepository.delete(
            db,
            order,
        )

        return {
            "message": "Order deleted successfully"
        }