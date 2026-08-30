from google import genai
import json

from ai_assistant.config import get_gemini_api_key, MODEL_NAME

_client = None


def get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=get_gemini_api_key())
    return _client


# This function is used to analyze the user query and decide whether an MCP tool is required or not
def analyze_query(
    user_query: str,
    available_tools,
    memory_context: str = "",
) -> str:
    """
    Gemini decides whether an MCP tool is required.
    If required, it selects the tool and arguments.
    Otherwise it responds directly.
    """

    prompt = f"""
You are an AI Shopping Assistant.

You can answer general questions and use MCP tools whenever live data or database operations are required.

==================================================
AVAILABLE MCP TOOLS
==================================================

{json.dumps(available_tools, indent=2)}

==================================================
CONVERSATION CONTEXT
==================================================

{memory_context}

==================================================
YOUR RESPONSIBILITIES
==================================================

1. Read the conversation context first.

2. Decide whether an MCP tool is required.

3. If a tool is required:
   - Select the SINGLE best tool.
   - Extract the correct arguments.
   - Return ONLY valid JSON.

4. If no tool is required:
   - Respond naturally.
   - Do not call any tool.

==================================================
WHEN TO USE MCP TOOLS
==================================================

Use MCP tools whenever the user wants:

• Search for products
• View product details
• List categories
• View user information
• Register a user
• Verify a user
• Place an order
• Retrieve live database information

PRODUCT SEARCH

Use search_products whenever the user's intent is to find or buy products.

==================================================
WHEN NOT TO USE MCP TOOLS
==================================================

Do NOT call any tool for:

• Greetings
• Thanks
• Asking who you are
• General conversation

Answer these directly.

==================================================
CONVERSATION MEMORY
==================================================

Always use the Conversation Context.

If a selected product already exists and the user says:
- buy it
- confirm
- this
- it

treat those references as the selected product.

Do NOT search for products again unless the user requests a different product.

--------------------------------------------------

If a Current User already exists,

Do NOT register the user again.

Reuse the stored user.

--------------------------------------------------

If no product is currently selected and the user mentions a product,

search for that product using search_products.

==================================================
IMPORTANT RULES
==================================================

• Never invent tool names.
• Never invent parameters.
• Use only parameters defined by the tool schema.
• Call only ONE tool per response.
• Use Conversation Context before making a decision.
• Prefer reusing memory instead of asking repeated questions.

==================================================
OUTPUT FORMAT
==================================================

If NO tool is needed:

{{
    "tool": null,
    "arguments": {{}},
    "response": "<natural response>"
}}

If a tool IS needed:

{{
    "tool": "<tool_name>",
    "arguments": {{
        ...
    }}
}}

Return ONLY valid JSON.

==================================================
USER REQUEST
==================================================

{user_query}
"""
    print("=" * 60)
    print(f"Using Gemini Model: {MODEL_NAME}")
    print("=" * 60)

    print(">>> Sending request to Gemini...")

    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    print(">>> Gemini responded.")

    return response.text

# This function is used to convert the raw MCP output into a natural language response

def summarize_response(
    user_query: str,
    tool_result: str,
) -> str:
    """
    Convert raw MCP output into a natural language response.
    """

    prompt = f"""
User Request:
{user_query}

Tool Result:
{tool_result}

Instructions:

- Use ONLY the tool result.
- Do NOT invent information.
- Present products as bullet points when appropriate.
- If no data exists, clearly state that.
- Keep the response concise and conversational.
"""

    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text