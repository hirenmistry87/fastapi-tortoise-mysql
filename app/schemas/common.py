from pydantic import BaseModel
from typing import Any, Optional


class ErrorDetail(BaseModel):
    code: str
    details: Optional[Any] = None


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: ErrorDetail
