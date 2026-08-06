from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.product_db import Base

#this class is used to define the Category model in the database
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False)

    description = Column(Text)

    # One Category -> Many Products
    products = relationship(
        "Product",
        back_populates="category",
        cascade="all, delete-orphan"
    )