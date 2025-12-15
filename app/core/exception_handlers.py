from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import IntegrityError

from app.schemas.common import ErrorResponse, ErrorDetail


def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            message=exc.detail,
            error=ErrorDetail(
                code="HTTP_ERROR",
                details=None,
            ),
        ).model_dump(),
    )


def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            message="Database integrity error",
            error=ErrorDetail(
                code="DB_INTEGRITY_ERROR",
                details=str(exc),
            ),
        ).model_dump(),
    )


def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            message="Internal server error",
            error=ErrorDetail(
                code="INTERNAL_ERROR",
                details=None,
            ),
        ).model_dump(),
    )

