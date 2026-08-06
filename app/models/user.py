from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.product_db import Base

#this class is used to define the User model in the database
class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    phone = Column(
    String(20),
    unique=True,
    nullable=False,
   )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )