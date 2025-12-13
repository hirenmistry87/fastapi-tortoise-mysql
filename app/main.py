from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM
from app.routers import users, employees, products, orders

app = FastAPI(title="FastAPI Tortoise MySQL (existing tables)")
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
