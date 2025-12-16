from typing import TypeVar, Generic, List, Optional, Tuple
from tortoise.queryset import QuerySet
from pydantic import BaseModel

T = TypeVar("T")


class PaginationMeta(BaseModel):
    total: Optional[int] = None
    skip: Optional[int] = None
    limit: int
    next_cursor: Optional[int] = None


class PaginatedResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: List[T]
    meta: PaginationMeta


async def paginate_offset(
    queryset: QuerySet,
    *,
    skip: int = 0,
    limit: int = 10,
    count_total: bool = True,
) -> Tuple[List, PaginationMeta]:
    total = await queryset.count() if count_total else None
    items = await queryset.offset(skip).limit(limit)
    return items, PaginationMeta(total=total, skip=skip, limit=limit)


async def paginate_cursor(
    queryset: QuerySet,
    *,
    limit: int = 10,
    cursor_field: str = "id",
    cursor: Optional[int] = None,
) -> Tuple[List, PaginationMeta]:

    if cursor is not None:
        queryset = queryset.filter(**{f"{cursor_field}__gt": cursor})

    queryset = queryset.order_by(cursor_field)
    items = await queryset.limit(limit)

    next_cursor = getattr(items[-1], cursor_field) if items else None

    return items, PaginationMeta(limit=limit, next_cursor=next_cursor)
