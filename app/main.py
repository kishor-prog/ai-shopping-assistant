from fastapi import FastAPI

from app.database.product_db import Base as ProductBase
from app.database.product_db import engine as ProductEngine

from app.database.order_db import Base as OrderBase
from app.database.order_db import engine as OrderEngine

from app.routes.category_routes import router as category_router
from app.routes.product_routes import router as product_router
from app.routes.inventory_routes import router as inventory_router
from app.routes.user_routes import router as user_router
from app.routes.order_routes import router as order_router

import app.models

ProductBase.metadata.create_all(bind=ProductEngine)
OrderBase.metadata.create_all(bind=OrderEngine)

app = FastAPI(
    title="MCP Backend Server",
    version="1.0.0",
)

# Register Category Routes
app.include_router(category_router)
app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(user_router)
app.include_router(order_router)


@app.get("/")
def root():
    return {
        "message": "MCP Backend Server Running"
    }