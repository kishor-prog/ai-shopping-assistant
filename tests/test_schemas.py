import pytest
from decimal import Decimal
from datetime import datetime

from app.schemas.category import CategoryCreate, CategoryResponse
from app.schemas.product import ProductCreate, ProductResponse
from app.schemas.user import UserCreate, UserResponse
from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.inventory import InventoryCreate, InventoryResponse


def test_category_schema():
    data = {"name": "Electronics", "description": "Gadgets and tech"}
    schema = CategoryCreate(**data)
    assert schema.name == "Electronics"
    assert schema.description == "Gadgets and tech"

    resp = CategoryResponse(id=1, name="Electronics", description="Gadgets and tech")
    assert resp.id == 1


def test_product_schema():
    data = {
        "name": "Wireless Mouse",
        "description": "Ergonomic bluetooth mouse",
        "price": Decimal("29.99"),
        "sku": "MOUSE-001",
        "category_id": 1,
    }
    schema = ProductCreate(**data)
    assert schema.name == "Wireless Mouse"
    assert schema.price == Decimal("29.99")
    assert schema.sku == "MOUSE-001"

    resp = ProductResponse(id=10, **data)
    assert resp.id == 10
    assert resp.sku == "MOUSE-001"


def test_user_schema():
    data = {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "phone": "9876543210",
    }
    schema = UserCreate(**data)
    assert schema.name == "Alice Smith"
    assert schema.phone == "9876543210"

    resp = UserResponse(id=1, created_at=datetime.now(), **data)
    assert resp.id == 1


def test_order_schema():
    data = {
        "user_id": 1,
        "product_id": 10,
        "quantity": 2,
    }
    schema = OrderCreate(**data)
    assert schema.quantity == 2

    resp = OrderResponse(id=100, created_at=datetime.now(), **data)
    assert resp.id == 100
    assert resp.quantity == 2


def test_inventory_schema():
    data = {
        "product_id": 10,
        "quantity": 50,
        "warehouse": "North Warehouse",
    }
    schema = InventoryCreate(**data)
    assert schema.quantity == 50

    resp = InventoryResponse(id=5, **data)
    assert resp.id == 5
    assert resp.warehouse == "North Warehouse"
