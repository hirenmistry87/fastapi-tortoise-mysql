from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models import User
from app.schemas import ApiResponse,UserCreate, UserRead    
from tortoise.exceptions import IntegrityError
from app.core.pagination import paginate_offset, paginate_cursor, PaginatedResponse
from app.core.orm_protection import protect_queryset

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=ApiResponse[UserRead])
async def create_user(payload: UserCreate):
    # Optional: normalize email
    payload.email = payload.email.lower().strip()

    try:
        user = await User.create(**payload.model_dump())
    except IntegrityError:
        # Handles race condition + DB unique constraint
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return ApiResponse(
        success=True,
        message="User created successfully",
        data=UserRead.model_validate(user),
    )


@router.get("/", response_model=PaginatedResponse[UserRead])
async def list_users(skip: int = 0, limit: int = 10):
    queryset = protect_queryset(
        User.all(),
        prefetch=["orders"],
    )

    users, meta = await paginate_offset(queryset, skip=skip, limit=limit)

    return PaginatedResponse(
        message="Users fetched successfully",
        data=[UserRead.model_validate(u) for u in users],
        meta=meta,
    )

@router.get("/{user_id}", response_model=ApiResponse[UserRead])
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return ApiResponse(
        success=True,
        message="User retrieved successfully",
        data=UserRead.model_validate(user),
    )


# ---------- UPDATE ----------
@router.patch("/{user_id}", response_model=ApiResponse[UserRead])
async def update_user(user_id: int, payload: UserCreate):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    await user.save()
    return ApiResponse(
        success=True,
        message="User updated successfully",
        data=UserRead.model_validate(user),
    )   


# ---------- DELETE ----------
@router.delete("/{user_id}", response_model=ApiResponse[dict])
async def delete_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    deleted = await User.filter(id=user_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return ApiResponse(
        success=True,
        message="User deleted successfully",
        data={"deleted": True},
    )