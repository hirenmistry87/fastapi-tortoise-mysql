from tortoise.queryset import QuerySet


def protect_queryset(
    queryset: QuerySet,
    *,
    select: list[str] | None = None,
    prefetch: list[str] | None = None,
) -> QuerySet:
    """
    Ensures required relations are loaded to avoid lazy-load crashes
    """

    if select:
        queryset = queryset.select_related(*select)

    if prefetch:
        queryset = queryset.prefetch_related(*prefetch)

    return queryset
