import pytest
from ai_assistant.chat_service import extract_json_response


def test_extract_pure_json():
    raw = '{"tool": "search_products", "arguments": {"keyword": "shoes"}}'
    parsed = extract_json_response(raw)
    assert parsed["tool"] == "search_products"
    assert parsed["arguments"]["keyword"] == "shoes"


def test_extract_markdown_fenced_json():
    raw = """```json
{
    "tool": "get_product",
    "arguments": {
        "product_id": 5
    }
}
```"""
    parsed = extract_json_response(raw)
    assert parsed["tool"] == "get_product"
    assert parsed["arguments"]["product_id"] == 5


def test_extract_json_with_filler_text():
    raw = """Here is the decision based on user input:
{
    "tool": null,
    "arguments": {},
    "response": "Hello! How can I assist your shopping today?"
}
Hope this helps!"""
    parsed = extract_json_response(raw)
    assert parsed["tool"] is None
    assert "Hello" in parsed["response"]
