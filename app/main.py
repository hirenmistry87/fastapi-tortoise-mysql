from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.exceptions import HTTPException
from tortoise.exceptions import IntegrityError

from app.config import TORTOISE_ORM
from app.routers import users, employees, products, orders

from app.core.exception_handlers import (
    http_exception_handler,
    integrity_error_handler,
    generic_exception_handler,
)

app = FastAPI(title="FastAPI Tortoise MySQL (existing tables)")

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(users.router)
app.include_router(employees.router)
app.include_router(products.router)
app.include_router(orders.router)
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Important: we won't auto-create schemas for existing tables
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    return {"ok": True}
