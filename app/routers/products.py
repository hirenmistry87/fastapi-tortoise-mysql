from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Product
from app.schemas import ApiResponse,ProductCreate, ProductRead
from app.core.pagination import paginate_offset, paginate_cursor, PaginatedResponse
from app.core.orm_protection import protect_queryset

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ApiResponse[ProductRead])
async def create_product(payload: ProductCreate):
    p = await Product.create(**payload.model_dump())
    return ApiResponse(
        success=True,
        message="Product created successfully",
        data=ProductRead.model_validate(p),
    )
    
@router.get("/", response_model=PaginatedResponse[ProductRead])
async def list_products(skip: int = 0, limit: int = 10):
    queryset = protect_queryset(
        Product.all(),
        prefetch=["order_items"],
    )

    products, meta = await paginate_offset(queryset, skip=skip, limit=limit)

    return PaginatedResponse(
        message="Products fetched successfully",
        data=[ProductRead.model_validate(p) for p in products],
        meta=meta,
    )

@router.get("/{product_id}", response_model=ApiResponse[ProductRead])
async def get_product(product_id: int):
    p = await Product.get_or_none(id=product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return ApiResponse(
        success=True,
        message="Product retrieved successfully",
        data=ProductRead.model_validate(p),
    )

@router.patch("/{product_id}", response_model=ApiResponse[ProductRead])
async def update_product(product_id: int, payload: ProductCreate):
    p = await Product.get_or_none(id=product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    # ✅ Pydantic v2 way
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(p, key, value)
    await p.save()
    return ApiResponse(
        success=True,
        message="Product updated successfully",
        data=ProductRead.model_validate(p),
    )

@router.delete("/{product_id}", response_model=ApiResponse[dict])
async def delete_product(product_id: int):
    p = await Product.get_or_none(id=product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted = await Product.filter(id=product_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return ApiResponse(
        success=True,
        message="Product deleted successfully",
        data={"deleted": True},
    )
