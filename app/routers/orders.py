from tortoise.transactions import in_transaction
from fastapi import APIRouter, HTTPException, Query
from typing import List

from app.models import Order, Product, OrderItem
from app.schemas import ApiResponse, OrderCreate, OrderRead, OrderUpdate
from app.core.pagination import paginate_cursor, PaginatedResponse
from app.core.orm_protection import protect_queryset

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=ApiResponse[OrderRead])
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
    return ApiResponse(
        success=True,
        message="Order created successfully",
        data=OrderRead.model_validate(order),
    )


@router.get("/", response_model=PaginatedResponse[OrderRead])
async def list_orders(
    cursor: int | None = Query(None),
    limit: int = Query(10),
):
    queryset = protect_queryset(
        Order.all(),
        select=["user"],
        prefetch=["items__product"],
    )

    orders, meta = await paginate_cursor(
        queryset,
        cursor=cursor,
        limit=limit,
    )

    return PaginatedResponse(
        message="Orders fetched successfully",
        data=[OrderRead.model_validate(o) for o in orders],
        meta=meta,
    )


@router.get("/{order_id}", response_model=ApiResponse[OrderRead])
async def get_order(order_id: int):

    order = (
        await Order
        .get_or_none(id=order_id)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return ApiResponse(
        success=True,
        message="Order retrieved successfully",
        data=OrderRead.model_validate(order),
    )

@router.patch("/{order_id}", response_model=ApiResponse[OrderRead])
async def update_order(order_id: int, payload: OrderUpdate):

    order = await Order.get_or_none(id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Update order fields
    update_data = payload.model_dump(exclude_unset=True, exclude={"items"})
    for key, value in update_data.items():
        setattr(order, key, value)

    await order.save()

    # Update items if included
    if payload.items:
        for item in payload.items:
            order_item = await OrderItem.get_or_none(order_id=order.id, product_id=item.product_id)
            if order_item:
                # Update existing item
                order_item.quantity = item.quantity
                order_item.price = item.price
                await order_item.save()
            else:
                # Create new item
                await OrderItem.create(
                    order_id=order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.price
                )

    # Reload order with relations for nested response
    order = (
        await Order
        .get(id=order.id)
        .select_related("user")
        .prefetch_related("items", "items__product")
    )
    return ApiResponse(
        success=True,
        message="Order updated successfully",
        data=OrderRead.model_validate(order),
    )

@router.delete("/{order_id}", response_model=ApiResponse[dict])
async def delete_order(order_id: int):
    order = await Order.get_or_none(id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    deleted = await Order.filter(id=order_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return ApiResponse(
        success=True,
        message="Order deleted successfully",
        data={"deleted": True},
    )
