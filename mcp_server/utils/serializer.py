from decimal import Decimal

def serialize_product(product):
    """Serialize SQLAlchemy Product model to dictionary."""
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": (
            float(product.price)
            if isinstance(product.price, Decimal)
            else product.price
        ),
        "sku": product.sku,
        "category_id": product.category_id,
        "created_at": (
            product.created_at.isoformat()
            if getattr(product, "created_at", None)
            else None
        ),
    }


def serialize_category(category):
    """Serialize SQLAlchemy Category model to dictionary."""
    return {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }


def serialize_user(user):
    """Serialize SQLAlchemy User model to dictionary."""
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "created_at": (
            user.created_at.isoformat()
            if getattr(user, "created_at", None)
            else None
        ),
    }


def serialize_order(order):
    """Serialize SQLAlchemy Order model to dictionary."""
    return {
        "id": order.id,
        "user_id": order.user_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "created_at": (
            order.created_at.isoformat()
            if getattr(order, "created_at", None)
            else None
        ),
    }


def serialize_inventory(inventory):
    """Serialize SQLAlchemy Inventory model to dictionary."""
    return {
        "id": inventory.id,
        "product_id": inventory.product_id,
        "quantity": inventory.quantity,
        "warehouse": inventory.warehouse,
        "updated_at": (
            inventory.updated_at.isoformat()
            if getattr(inventory, "updated_at", None)
            else None
        ),
    }