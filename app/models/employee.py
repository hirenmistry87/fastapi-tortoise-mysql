from typing import TYPE_CHECKING
from tortoise import fields, models

if TYPE_CHECKING:
    from .user import User

class Employee(models.Model):
    id = fields.IntField(pk=True)

    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User",
        related_name="employees"
    )

    name = fields.CharField(max_length=191)
    role = fields.CharField(max_length=100, null=True)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "employees"
