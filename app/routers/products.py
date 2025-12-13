from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Product
from app.schemas import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductRead)
async def create_product(payload: ProductCreate):
    p = await Product.create(**payload.model_dump())
    # ✅ Convert ORM object directly (NO re-query, NO error)
    return ProductRead.model_validate(p)

@router.get("/", response_model=List[ProductRead])
async def list_products(skip: int = 0, limit: int = 100):
    return await ProductRead.from_queryset(
        Product.all().offset(skip).limit(limit)
    )

@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: int):
    p = await Product.get_or_none(id=product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead.model_validate(p)


@router.patch("/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, payload: ProductCreate):
    p = await Product.get_or_none(id=product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    # ✅ Pydantic v2 way
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(p, key, value)
    await p.save()
    return ProductRead.model_validate(p)


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    deleted = await Product.filter(id=product_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"deleted": True}
