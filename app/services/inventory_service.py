from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.inventory_repository import InventoryRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.inventory import InventoryCreate


class InventoryService:

    @staticmethod
    def create_inventory(
        db: Session,
        inventory: InventoryCreate
    ):
        # Check if product exists
        product = ProductRepository.get_by_id(
            db,
            inventory.product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        # Check if inventory already exists
        existing_inventory = InventoryRepository.get_by_product_id(
            db,
            inventory.product_id
        )

        if existing_inventory:
            raise HTTPException(
                status_code=400,
                detail="Inventory already exists for this product."
            )

        return InventoryRepository.create(
            db,
            inventory
        )

    @staticmethod
    def get_inventories(db: Session):
        return InventoryRepository.get_all(db)

    @staticmethod
    def get_inventory(
        db: Session,
        inventory_id: int
    ):
        inventory = InventoryRepository.get_by_id(
            db,
            inventory_id
        )

        if not inventory:
            raise HTTPException(
                status_code=404,
                detail="Inventory not found."
            )

        return inventory

    @staticmethod
    def update_inventory(
        db: Session,
        inventory_id: int,
        data: InventoryCreate
    ):
        inventory = InventoryRepository.get_by_id(
            db,
            inventory_id
        )

        if not inventory:
            raise HTTPException(
                status_code=404,
                detail="Inventory not found."
            )

        # Check if product exists
        product = ProductRepository.get_by_id(
            db,
            data.product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found."
            )

        # Check if another inventory record already uses this product
        existing_inventory = InventoryRepository.get_by_product_id(
            db,
            data.product_id
        )

        if (
            existing_inventory
            and existing_inventory.id != inventory_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Inventory already exists for this product."
            )

        return InventoryRepository.update(
            db,
            inventory,
            data
        )

    @staticmethod
    def delete_inventory(
        db: Session,
        inventory_id: int
    ):
        inventory = InventoryRepository.get_by_id(
            db,
            inventory_id
        )

        if not inventory:
            raise HTTPException(
                status_code=404,
                detail="Inventory not found."
            )

        InventoryRepository.delete(
            db,
            inventory
        )

        return {
            "message": "Inventory deleted successfully"
        }