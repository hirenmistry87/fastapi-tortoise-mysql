from typing import TYPE_CHECKING
from tortoise import fields, models
if TYPE_CHECKING:
    from .order_item import OrderItem

class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=191)
    description = fields.TextField(null=True)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    order_items: fields.ReverseRelation["OrderItem"]

    class Meta:
        table = "products"
