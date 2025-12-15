from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from .base import ReadBase

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal


class ProductRead(ReadBase):
    id: int
    name: str
    description: Optional[str]
    price: Decimal

    model_config = {"from_attributes": True}
