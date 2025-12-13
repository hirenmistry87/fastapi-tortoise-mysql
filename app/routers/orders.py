from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Order
from app.schemas import OrderCreate, OrderRead

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderRead)
async def create_order(payload: OrderCreate):
    o = await Order.create(**payload.model_dump())
    return OrderRead.model_validate(o)


@router.get("/", response_model=List[OrderRead])
async def list_orders(skip: int = 0, limit: int = 100):
    return await OrderRead.from_queryset(
        Order.all().offset(skip).limit(limit)
    )

@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: int):
    o = await Order.get_or_none(id=order_id).first()
    if not o:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderRead.model_validate(o)


@router.patch("/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, payload: OrderCreate):
    o = await Order.get_or_none(id=order_id).first()
    if not o:
        raise HTTPException(status_code=404, detail="Order not found")
     # ✅ Pydantic v2 way
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(o, key, value)
    await o.save()
    return OrderRead.model_validate(o)


@router.delete("/{order_id}")
async def delete_order(order_id: int):
    deleted = await Order.filter(id=order_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"deleted": True}
