from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import User, Employee, Product, Order


# ---------- USER SCHEMAS ----------

# ---------- INPUT SCHEMA ----------
class UserCreate(BaseModel):
    email: str
    full_name: Optional[str] = None
    is_active: Optional[bool] = True


# ---------- OUTPUT SCHEMA ----------
UserRead = pydantic_model_creator(
    User,
    name="UserRead",
)

# ---------- EMPLOYEE SCHEMAS ----------

# ---------- INPUT SCHEMA ----------
class EmployeeCreate(BaseModel):
    user_id: int
    name: str
    role: Optional[str]
    is_active: Optional[bool] = True

# ---------- OUTPUT SCHEMA ----------
EmployeeRead = pydantic_model_creator(
    Employee,
    name="EmployeeRead",
)

# ---------- PRODUCT SCHEMAS ----------

# ---------- INPUT SCHEMA ----------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: Decimal

# ---------- OUTPUT SCHEMA ----------
ProductRead = pydantic_model_creator(
    Product,
    name="ProductRead",
)

# ---------- ORDER SCHEMAS ----------

# ---------- INPUT SCHEMA ----------
class OrderCreate(BaseModel):
    user_id: Optional[int]
    total: Decimal

# ---------- OUTPUT SCHEMA ----------
OrderRead = pydantic_model_creator(
    Order,
    name="OrderRead",
)  
