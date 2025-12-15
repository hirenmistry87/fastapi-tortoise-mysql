from tortoise.transactions import in_transaction
from fastapi import APIRouter, HTTPException
from typing import List

from app.models import Order, Product, OrderItem
from app.schemas import OrderCreate, OrderRead, OrderUpdate

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderRead)
async def create_order(data: OrderCreate):

    async with in_transaction() as conn:

        order = await Order.create(
            user_id=data.user_id,
            total=data.total,
            using_db=conn
        )

        for item in data.items:
            product = await Product.get_or_none(
                id=item.product_id,
                using_db=conn
            )

            if not product:
                raise HTTPException(
                    status_code=400,
                    detail=f"Product {item.product_id} not found"
                )

            await OrderItem.create(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price,
                using_db=conn
            )

    order = (
        await Order
        .get(id=order.id)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )

    return await OrderRead.from_tortoise_orm(order)


@router.get("/", response_model=List[OrderRead])
async def list_orders(skip: int = 0, limit: int = 100):
    orders = (
        await Order
        .all()
        .offset(skip)
        .limit(limit)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )
    return [OrderRead.model_validate(o) for o in orders]


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: int):

    order = (
        await Order
        .get_or_none(id=order_id)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return OrderRead.model_validate(order)


@router.patch("/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, payload: OrderUpdate):

    order = await Order.get_or_none(id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(order, key, value)

    await order.save()

    order = (
        await Order
        .get(id=order.id)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )

    return await OrderRead.from_tortoise_orm(order)


@router.delete("/{order_id}")
async def delete_order(order_id: int):

    deleted = await Order.filter(id=order_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"deleted": True}
