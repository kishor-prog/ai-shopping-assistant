from sqlalchemy.orm import Session

from app.models.order import Order
from app.schemas.order import OrderCreate

#this class is used to interact with the Order table in the database with methods to create, get, and delete orders
class OrderRepository:

    @staticmethod
    def create(
        db: Session,
        order: OrderCreate,
    ):
        db_order = Order(
            user_id=order.user_id,
            product_id=order.product_id,
            quantity=order.quantity,
        )

        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        return db_order

    @staticmethod
    def get_all(db: Session):
        return db.query(Order).all()

    @staticmethod
    def get_by_id(
        db: Session,
        order_id: int,
    ):
        return (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

    @staticmethod
    def get_by_user(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Order)
            .filter(Order.user_id == user_id)
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        order: Order,
    ):
        db.delete(order)
        db.commit()