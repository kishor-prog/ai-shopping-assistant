from decimal import Decimal

#this function is used to serialize the product object into a dictionary
def serialize_product(product):
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
    }

#this function is used to serialize the order object into a dictionary
def serialize_category(category):
    return {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }

#this function is used to serialize the order object into a dictionary
def serialize_user(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "created_at": (
            user.created_at.isoformat()
            if user.created_at
            else None
        ),
    }