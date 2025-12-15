from pydantic import BaseModel
from decimal import Decimal
from .product import ProductRead
from .base import ReadBase

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: Decimal


class OrderItemRead(ReadBase):
    id: int
    quantity: int
    price: Decimal
    product: ProductRead

    model_config = {"from_attributes": True}


class OrderItemUpdate(BaseModel):
    product_id: int
    quantity: int
    price: Decimal
