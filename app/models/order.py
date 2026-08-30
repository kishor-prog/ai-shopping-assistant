from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

from app.database.order_db import Base

# This class defines the Order model in the order database
class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # User ID from Order Database
    user_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    # Product ID from Product Database
    # Stored as integer because Product is in another database
    product_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )