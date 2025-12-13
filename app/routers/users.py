from fastapi import APIRouter, HTTPException
from typing import List
from app.models import User
from app.schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])


# ---------- CREATE ----------
@router.post("/", response_model=UserRead)
async def create_user(payload: UserCreate):
    if await User.filter(email=payload.email).exists():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = await User.create(**payload.model_dump())

    # ✅ Convert ORM object directly (NO re-query, NO error)
    return UserRead.model_validate(user)


# ---------- LIST ----------
@router.get("/", response_model=List[UserRead])
async def list_users(skip: int = 0, limit: int = 100):
    return await UserRead.from_queryset(
        User.all().offset(skip).limit(limit)
    )


# ---------- GET BY ID ----------
@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserRead.model_validate(user)


# ---------- UPDATE ----------
@router.patch("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, payload: UserCreate):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # ✅ Pydantic v2 way
    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    await user.save()

    # ✅ Convert ORM object directly
    return UserRead.model_validate(user)



# ---------- DELETE ----------
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    deleted = await User.filter(id=user_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}
