from typing import TYPE_CHECKING
from tortoise import fields, models

if TYPE_CHECKING:
    from .order import Order
    from .product import Product

class OrderItem(models.Model):
    id = fields.IntField(pk=True)

    order: fields.ForeignKeyRelation["Order"] = fields.ForeignKeyField(
        "models.Order",
        related_name="items"
    )

    product: fields.ForeignKeyRelation["Product"] = fields.ForeignKeyField(
        "models.Product",
        related_name="order_items"
    )

    quantity = fields.IntField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table = "order_items"
