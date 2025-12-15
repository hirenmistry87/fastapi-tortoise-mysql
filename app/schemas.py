from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import User, Employee, Product, Order, OrderItem


# ---------- USER ----------
class UserCreate(BaseModel):
    email: str
    full_name: Optional[str] = None
    is_active: bool = True


class UserRead(BaseModel):
    id: int
    email: str
    full_name: str | None
    is_active: bool

    model_config = {"from_attributes": True}

# ---------- EMPLOYEE ----------
class EmployeeCreate(BaseModel):
    user_id: int
    name: str
    role: Optional[str] = None
    is_active: bool = True


class EmployeeRead(BaseModel):
    id: int
    name: str
    role: str | None
    is_active: bool
    user: UserRead

    model_config = {"from_attributes": True}


# ---------- PRODUCT ----------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal


class ProductRead(BaseModel):
    id: int
    name: str
    price: Decimal

    model_config = {"from_attributes": True}


# ---------- ORDER ITEM ----------
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: Decimal


class OrderItemRead(BaseModel):
    id: int
    quantity: int
    price: Decimal
    product: ProductRead

    model_config = {"from_attributes": True}


# ---------- ORDER ----------
class OrderCreate(BaseModel):
    user_id: int
    total: Decimal
    items: List[OrderItemCreate]


class OrderRead(BaseModel):
    id: int
    total: Decimal
    user: UserRead | None
    items: list[OrderItemRead]

    model_config = {"from_attributes": True}

class OrderUpdate(BaseModel):
    total: Optional[Decimal] = None