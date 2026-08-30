from datetime import datetime
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)