from pydantic import BaseModel


class InventoryCreate(BaseModel):
    product_id: int
    quantity: int
    warehouse: str


class InventoryResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    warehouse: str

    class Config:
        from_attributes = True