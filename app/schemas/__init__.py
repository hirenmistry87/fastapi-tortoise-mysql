# Note : as all schemas are very lightweight, we can import them all here for easier access
from .base import ReadBase
from .response import ApiResponse
from .user import UserCreate, UserRead
from .employee import EmployeeCreate, EmployeeRead
from .product import ProductCreate, ProductRead
from .order_item import (
    OrderItemCreate,
    OrderItemRead,
    OrderItemUpdate,
)
from .order import OrderCreate, OrderRead, OrderUpdate

__all__ = [
    "ReadBase", "ApiResponse",
    "UserCreate", "UserRead",
    "EmployeeCreate", "EmployeeRead",
    "ProductCreate", "ProductRead",
    "OrderItemCreate", "OrderItemRead", "OrderItemUpdate",
    "OrderCreate", "OrderRead", "OrderUpdate",
]
