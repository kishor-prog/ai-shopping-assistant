from pydantic import BaseModel, ConfigDict


class InventoryBase(BaseModel):
    product_id: int
    quantity: int = 0
    warehouse: str | None = None


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    product_id: int | None = None
    quantity: int | None = None
    warehouse: str | None = None


class InventoryResponse(InventoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)