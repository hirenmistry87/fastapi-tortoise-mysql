from fastapi import APIRouter, HTTPException
from typing import List
from app.models import User
from app.schemas import UserCreate, UserRead    
from tortoise.exceptions import IntegrityError

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
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

    return UserRead.model_validate(user)


@router.get("/", response_model=list[UserRead])
async def list_users(skip: int = 0, limit: int = 100):

    users = await User.all().offset(skip).limit(limit)

    return [UserRead.model_validate(u) for u in users]


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
