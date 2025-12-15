from typing import TYPE_CHECKING
from tortoise import fields, models

if TYPE_CHECKING:
    from .employee import Employee
    from .order import Order

class User(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=191, unique=True, index=True)
    full_name = fields.CharField(max_length=191, null=True)
    is_active = fields.BooleanField(default=True)

    employees: fields.ReverseRelation["Employee"]
    orders: fields.ReverseRelation["Order"]

    class Meta:
        table = "users"
