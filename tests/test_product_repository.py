import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from decimal import Decimal

from app.database.product_db import Base
from app.models.category import Category
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository


@pytest.fixture
def db_session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Seed Category
    cat = CategoryRepository.create(session, name="Electronics", description="Electronic items")

    # Seed Products
    ProductRepository.create(
        session,
        ProductCreate(
            name="Studio Headphones",
            description="High quality over-ear headphones",
            price=Decimal("150.00"),
            sku="AUDIO-001",
            category_id=cat.id,
        ),
    )
    ProductRepository.create(
        session,
        ProductCreate(
            name="Budget Earbuds",
            description="Affordable in-ear headphones",
            price=Decimal("30.00"),
            sku="AUDIO-002",
            category_id=cat.id,
        ),
    )
    ProductRepository.create(
        session,
        ProductCreate(
            name="Gaming Mouse",
            description="RGB optical mouse",
            price=Decimal("45.00"),
            sku="MOUSE-001",
            category_id=cat.id,
        ),
    )

    yield session
    session.close()


def test_search_exact_match_with_price_filter(db_session):
    # Studio Headphones costs 150.00. With max_price=100, Studio Headphones must NOT be returned.
    results = ProductRepository.search(
        db=db_session,
        keyword="Studio Headphones",
        max_price=100.0,
    )
    names = [r.name for r in results]
    assert "Studio Headphones" not in names

    # With max_price=200, Studio Headphones should match
    results = ProductRepository.search(
        db=db_session,
        keyword="Studio Headphones",
        max_price=200.0,
    )
    assert len(results) >= 1
    assert results[0].name == "Studio Headphones"


def test_search_keyword_and_category(db_session):
    # Search "headphones" (plural normalized to singular)
    results = ProductRepository.search(
        db=db_session,
        keyword="headphones",
    )
    assert len(results) >= 1
    names = [r.name for r in results]
    assert "Studio Headphones" in names

    # Search category Electronics
    results = ProductRepository.search(
        db=db_session,
        keyword="Electronics",
    )
    assert len(results) == 3


def test_search_price_range_only(db_session):
    results = ProductRepository.search(
        db=db_session,
        min_price=40.0,
        max_price=160.0,
    )
    names = [r.name for r in results]
    assert "Gaming Mouse" in names
    assert "Studio Headphones" in names
    assert "Budget Earbuds" not in names
