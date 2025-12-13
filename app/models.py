from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=191, unique=True)
    full_name = fields.CharField(max_length=191, null=True)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "users"


class Employee(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()  # foreign key column in existing table
    name = fields.CharField(max_length=191)
    role = fields.CharField(max_length=100, null=True)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "employees"


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=191)
    description = fields.TextField(null=True)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "products"


class Order(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField(null=True)
    total = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "orders"
