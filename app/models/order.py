from typing import TYPE_CHECKING
from tortoise import fields, models

if TYPE_CHECKING:
    from .user import User
    from .order_item import OrderItem

class Order(models.Model):
    id = fields.IntField(pk=True)

    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User",
        related_name="orders",
        index=True
    )

    total = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True,index=True)
    updated_at = fields.DatetimeField(auto_now=True)

    items: fields.ReverseRelation["OrderItem"]

    class Meta:
        table = "orders"
