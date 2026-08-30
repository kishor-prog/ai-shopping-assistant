import pytest
from decimal import Decimal
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import app.models
from app.main import app
from app.database.dependencies import get_product_db, get_order_db
from app.database.product_db import Base as ProductBase
from app.database.order_db import Base as OrderBase

# Test databases using StaticPool so all connections share the in-memory database
prod_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
order_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

ProductBase.metadata.create_all(bind=prod_engine)
OrderBase.metadata.create_all(bind=order_engine)

ProdSession = sessionmaker(bind=prod_engine)
OrderSession = sessionmaker(bind=order_engine)


def override_get_product_db():
    db = ProdSession()
    try:
        yield db
    finally:
        db.close()


def override_get_order_db():
    db = OrderSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_product_db] = override_get_product_db
app.dependency_overrides[get_order_db] = override_get_order_db

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "MCP Backend Server Running"}


def test_category_and_product_flow():
    # 1. Create Category
    cat_res = client.post("/categories/", json={"name": "Books", "description": "Reading materials"})
    assert cat_res.status_code == 200
    cat_data = cat_res.json()
    cat_id = cat_data["id"]

    # 2. Create Product
    prod_res = client.post(
        "/products/",
        json={
            "name": "Python Guide",
            "description": "Learn python programming",
            "price": "39.99",
            "sku": "BOOK-001",
            "category_id": cat_id,
        },
    )
    assert prod_res.status_code == 200
    prod_data = prod_res.json()
    assert prod_data["name"] == "Python Guide"

    # 3. Search Product
    search_res = client.get("/products/search?keyword=Python")
    assert search_res.status_code == 200
    results = search_res.json()
    assert len(results) >= 1
    assert results[0]["sku"] == "BOOK-001"


def test_user_and_order_flow():
    # 1. Create User
    user_res = client.post(
        "/users/",
        json={
            "name": "Bob Builder",
            "email": "bob@example.com",
            "phone": "5551234567",
        },
    )
    assert user_res.status_code == 200
    user_data = user_res.json()
    user_id = user_data["id"]

    # 2. Lookup by phone
    phone_res = client.get(f"/users/phone/{user_data['phone']}")
    assert phone_res.status_code == 200
    assert phone_res.json()["name"] == "Bob Builder"
