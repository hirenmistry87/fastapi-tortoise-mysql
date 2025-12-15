from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

from .user import UserRead
from .order_item import OrderItemCreate, OrderItemRead, OrderItemUpdate
from .base import ReadBase

class OrderCreate(BaseModel):
    user_id: int
    total: Decimal
    items: List[OrderItemCreate]


class OrderRead(ReadBase):
    id: int
    total: Decimal
    user: Optional[UserRead]
    items: List[OrderItemRead]

    model_config = {"from_attributes": True}


class OrderUpdate(BaseModel):
    user_id: Optional[int]
    total: Optional[Decimal]
    items: Optional[List[OrderItemUpdate]]
