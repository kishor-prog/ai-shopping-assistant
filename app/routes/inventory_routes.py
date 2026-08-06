from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_product_db
from app.schemas.inventory import InventoryCreate, InventoryResponse
from app.services.inventory_service import InventoryService

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/", response_model=InventoryResponse)
def create_inventory(
    inventory: InventoryCreate,
    db: Session = Depends(get_product_db),
):
    return InventoryService.create_inventory(
        db,
        inventory,
    )


@router.get("/", response_model=list[InventoryResponse])
def get_inventories(
    db: Session = Depends(get_product_db),
):
    return InventoryService.get_inventories(db)


@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory(
    inventory_id: int,
    db: Session = Depends(get_product_db),
):
    return InventoryService.get_inventory(
        db,
        inventory_id,
    )


@router.put("/{inventory_id}", response_model=InventoryResponse)
def update_inventory(
    inventory_id: int,
    inventory: InventoryCreate,
    db: Session = Depends(get_product_db),
):
    return InventoryService.update_inventory(
        db,
        inventory_id,
        inventory,
    )


@router.delete("/{inventory_id}")
def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_product_db),
):
    return InventoryService.delete_inventory(
        db,
        inventory_id,
    )