from pydantic import BaseModel
from typing import Optional
from .base import ReadBase

class UserCreate(BaseModel):
    email: str
    full_name: Optional[str] = None
    is_active: bool = True


class UserRead(ReadBase):
    id: int
    email: str
    full_name: Optional[str]
    is_active: bool

    model_config = {"from_attributes": True}
