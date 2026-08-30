import pytest
from ai_assistant.conversation_memory import ConversationMemory


def test_conversation_memory_initial_state():
    memory = ConversationMemory()
    assert memory.get_state() == "idle"
    assert memory.get_selected_product() is None
    assert memory.get_current_user() is None
    assert memory.get_pending_order() is None


def test_conversation_memory_product_and_user_flow():
    memory = ConversationMemory()

    product = {"id": 1, "name": "Studio Headphones", "price": 199.99}
    memory.set_selected_product(product)
    assert memory.get_selected_product() == product

    user = {"id": 42, "name": "John Doe", "email": "john@example.com", "phone": "1234567890"}
    memory.set_current_user(user)
    assert memory.get_current_user() == user

    memory.set_state("ready_to_create_order")
    assert memory.get_state() == "ready_to_create_order"

    memory.set_pending_order({"product_id": 1, "quantity": 2})
    assert memory.get_pending_order() == {"product_id": 1, "quantity": 2}

    memory.clear()
    assert memory.get_state() == "idle"
    assert memory.get_selected_product() is None
    assert memory.get_current_user() is None
    assert memory.get_pending_order() is None


def test_conversation_memory_pending_user():
    memory = ConversationMemory()
    memory.set_pending_name("Jane")
    memory.set_pending_phone("9998887777")
    memory.set_pending_email("jane@example.com")

    pending = memory.get_pending_user()
    assert pending["name"] == "Jane"
    assert pending["phone"] == "9998887777"
    assert pending["email"] == "jane@example.com"

    memory.clear_pending_user()
    assert memory.get_pending_user()["name"] is None
