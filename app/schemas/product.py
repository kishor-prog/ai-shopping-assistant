from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    sku: str
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    sku: str
    category_id: int

    class Config:
        from_attributes = True