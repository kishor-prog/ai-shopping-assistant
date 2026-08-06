from datetime import datetime

from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1


class OrderResponse(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True