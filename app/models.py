from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=191, unique=True, index=True)
    full_name = fields.CharField(max_length=191, null=True)
    is_active = fields.BooleanField(default=True)

    orders: fields.ReverseRelation["Order"]
    employees: fields.ReverseRelation["Employee"]

    class Meta:
        table = "users"


class Employee(models.Model):
    id = fields.IntField(pk=True)

    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User",
        related_name="employees",
        source_field="user_id"
    )

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

    order_items: fields.ReverseRelation["OrderItem"]

    class Meta:
        table = "products"


class Order(models.Model):
    id = fields.IntField(pk=True)

    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User",
        related_name="orders",
        source_field="user_id",
        null=True
    )

    total = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    items: fields.ReverseRelation["OrderItem"]

    class Meta:
        table = "orders"


class OrderItem(models.Model):
    id = fields.IntField(pk=True)

    order: fields.ForeignKeyRelation[Order] = fields.ForeignKeyField(
        "models.Order",
        related_name="items"
    )

    product: fields.ForeignKeyRelation[Product] = fields.ForeignKeyField(
        "models.Product",
        related_name="order_items"
    )

    quantity = fields.IntField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table = "order_items"
