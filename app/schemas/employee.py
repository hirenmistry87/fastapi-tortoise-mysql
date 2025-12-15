from pydantic import BaseModel
from typing import Optional
from .user import UserRead
from .base import ReadBase

class EmployeeCreate(BaseModel):
    user_id: int
    name: str
    role: Optional[str] = None
    is_active: bool = True


class EmployeeRead(ReadBase):
    id: int
    name: str
    role: Optional[str]
    is_active: bool
    user: UserRead

    model_config = {"from_attributes": True}
