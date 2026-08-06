from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Numeric,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.product_db import Base

#this class is used to define the Product model in the database
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    description = Column(Text)

    price = Column(Numeric(10, 2), nullable=False)

    sku = Column(
        String(50),
        unique=True,
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    category = relationship(
        "Category",
        back_populates="products"
    )