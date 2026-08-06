from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate


class InventoryRepository:

    @staticmethod
    def create(
        db: Session,
        inventory: InventoryCreate
    ):
        db_inventory = Inventory(
            product_id=inventory.product_id,
            quantity=inventory.quantity,
            warehouse=inventory.warehouse
        )

        db.add(db_inventory)
        db.commit()
        db.refresh(db_inventory)

        return db_inventory

    @staticmethod
    def get_all(db: Session):
        return db.query(Inventory).all()

    @staticmethod
    def get_by_id(
        db: Session,
        inventory_id: int
    ):
        return (
            db.query(Inventory)
            .filter(Inventory.id == inventory_id)
            .first()
        )

    @staticmethod
    def get_by_product_id(
        db: Session,
        product_id: int
    ):
        return (
            db.query(Inventory)
            .filter(Inventory.product_id == product_id)
            .first()
        )

    # Alias for OrderService
    @staticmethod
    def get_inventory_by_product_id(
        db: Session,
        product_id: int
    ):
        return (
            db.query(Inventory)
            .filter(Inventory.product_id == product_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        db_inventory: Inventory,
        inventory: InventoryCreate
    ):
        db_inventory.product_id = inventory.product_id
        db_inventory.quantity = inventory.quantity
        db_inventory.warehouse = inventory.warehouse

        db.commit()
        db.refresh(db_inventory)

        return db_inventory

    @staticmethod
    def delete(
        db: Session,
        db_inventory: Inventory
    ):
        db.delete(db_inventory)
        db.commit()