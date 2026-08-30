import json
import re
import traceback

from ai_assistant.config import MODEL_NAME
from ai_assistant.gemini_client import (
    analyze_query,
    summarize_response,
)
from ai_assistant.mcp_client import MCPClient
from ai_assistant.conversation_memory import ConversationMemory


def extract_json_response(raw_text: str) -> dict:
    """Extract and parse JSON from Gemini's response safely."""
    cleaned = raw_text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        # Match outermost JSON object { ... }
        match = re.search(r"(\{.*\})", cleaned, flags=re.DOTALL)
        if match:
            return json.loads(match.group(1))
        raise


class ChatService:

    def __init__(self):
        self.mcp = MCPClient()
        self.memory = ConversationMemory()

    # ==========================================================
    # Conversation State Machine
    # ==========================================================

    async def handle_state(
        self,
        user_query: str,
    ):

        state = self.memory.get_state()

        print("\n========== STATE ==========")
        print(state)
        print("===========================\n")

        # --------------------------------------------------
        # IDLE
        # --------------------------------------------------

        if state == "idle":

           checkout_phrases = [
               "buy it",
               "buy this",
               "purchase it",
               "purchase this",
               "checkout",
               "confirm",
               "place order",
          ] 

           if any(
             phrase in user_query.lower()
             for phrase in checkout_phrases
            ):

                product = self.memory.get_selected_product()

                if product is None:

                   return None

                user = self.memory.get_current_user()

                # Existing user
                if user is not None:

                    self.memory.set_pending_order(
                        {
                            "product_id": product["id"],
                            "quantity": 1,
                        }
                    )

                    self.memory.set_state(
                        "ready_to_create_order"
                    )

                    return (
                        "Type **confirm** to place your order."
                    )

                # Save pending order
                self.memory.set_pending_order(
                    {
                        "product_id": product["id"],
                        "quantity": 1,
                    }
                )

                # Ask phone number first
                self.memory.set_state(
                    "waiting_phone"
                )

                return (
                    f"You selected **{product['name']}**.\n\n"
                    "Before placing your order,\n"
                    "please enter your phone number."
                )

        # --------------------------------------------------
        # WAITING EMAIL
        # --------------------------------------------------

        if state == "waiting_email":

            self.memory.set_pending_email(
                user_query.strip()
            )

            user_data = self.memory.get_pending_user()

            tool_result = await self.mcp.execute(
                "create_user",
                user_data,
            )

            user = json.loads(tool_result[0])

            self.memory.set_current_user(user)

            self.memory.set_state(
                "ready_to_create_order"
            )

            return (
                f"✅ Welcome {user['name']}!\n\n"
                "Type **confirm** to place your order."
            )

        # --------------------------------------------------
        # WAITING PHONE
        # --------------------------------------------------

        if self.memory.get_state() == "waiting_phone":

            phone = user_query.strip()

            # Validate phone number
            if not phone.isdigit() or len(phone) != 10:
                return (
                    "Please enter a valid 10-digit phone number."
                )

            try:
                tool_result = await self.mcp.execute(
                    "get_user_by_phone",
                    {
                        "phone": phone,
                    },
                )

                if tool_result:

                    user = json.loads(tool_result[0])

                    self.memory.set_current_user(user)

                    self.memory.set_pending_phone(phone)

                    self.memory.set_state(
                        "ready_to_create_order"
                    )

                    return (
                        f"👋 Welcome back {user['name']}!\n\n"
                        "Type **confirm** to place your order."
                    )

            except Exception as e:

                print("User lookup:", e)

                # User not found → begin registration
                self.memory.set_pending_phone(phone)

                self.memory.set_state(
                    "waiting_name"
                )

                return (
                    "It looks like you're a new customer.\n\n"
                    "What is your name?"
                )

        # --------------------------------------------------
        # WAITING NAME
        # --------------------------------------------------

        if state == "waiting_name":

           self.memory.set_pending_name(
               user_query.strip()
           )

           self.memory.set_state(
               "waiting_email"
           )

           return (
               "Great!\n\n"
               "What is your email address?"
         )

        # --------------------------------------------------
        # READY TO CREATE ORDER
        # --------------------------------------------------

        if state == "ready_to_create_order":

            if user_query.lower().strip() not in [
                "confirm",
                "yes",
                "place order",
            ]:

                return (
                    "Please type **confirm** to place your order."
                )

            user = self.memory.get_current_user()
            order = self.memory.get_pending_order()

            tool_result = await self.mcp.execute(
                "create_order",
                {
                    "user_id": user["id"],
                    "product_id": order["product_id"],
                    "quantity": order["quantity"],
                },
            )

            self.memory.clear()

            return (
                "🎉 Your order has been placed successfully!"
            )

        return None

    # ==========================================================
    # Main Chat Function
    # ==========================================================
#this class handels the user query and reach the gemini function to analyze the query
#after this it get the available tools from MCP server and build the memory context
#after this two step gemini decides which tool to use for the user query and convert the query to json format for MCP sever to understand it
#after this step it send the request to MCP server and get result and update the memory state

    async def chat(
        self,
        user_query: str,
    ) -> str:

        try:

            # ---------------------------------
            # Handle Conversation State
            # ---------------------------------

            state_response = await self.handle_state(
                user_query,
            )

            if state_response:
                return state_response

            print("Reached Gemini Decision")



            # ---------------------------------
            # Get Available MCP Tools
            # ---------------------------------

            tools = await self.mcp.list_tools()

            tool_info = []

            for tool in tools:

                tool_info.append(
                    {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema,
                    }
                )

            # ---------------------------------
            # Build Memory Context
            # ---------------------------------

            memory_context = ""

            product = self.memory.get_selected_product()

            if product:

                memory_context += (
                    f"Selected Product:\n"
                    f"ID: {product['id']}\n"
                    f"Name: {product['name']}\n"
                    f"Price: {product['price']}\n\n"
                )

            user = self.memory.get_current_user()

            if user:

                memory_context += (
                    f"Current User:\n"
                    f"ID: {user['id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n\n"
                )

            print("\n========== MEMORY ==========")
            print(memory_context if memory_context else "Empty")
            print("============================\n")

            # ---------------------------------
            # Gemini decides the tool
            # ---------------------------------

            decision = analyze_query(
                user_query,
                tool_info,
                memory_context,
            )

            print("\n========== RAW GEMINI RESPONSE ==========")
            print(decision)
            print("=========================================\n")

            decision_dict = extract_json_response(decision)

            tool_name = decision_dict.get("tool")
            arguments = decision_dict.get(
                "arguments",
                {},
            )

            print("\n========== GEMINI ==========")
            print(
                json.dumps(
                    decision_dict,
                    indent=4,
                )
            )
            print("============================\n")

            # ---------------------------------
            # No Tool Needed
            # ---------------------------------

            if tool_name is None:

                return decision_dict.get(
                    "response",
                    "How can I help you?",
                )

            # ---------------------------------
            # Execute MCP Tool
            # ---------------------------------

            tool_result = await self.mcp.execute(
                tool_name,
                arguments,
            )

            print("\n========== MCP RESULT ==========")
            print(tool_result)
            print("================================\n")

            if not tool_result:
                return (
                    f"Sorry, I couldn't find any products matching '{user_query}'."
                )

            # ---------------------------------
            # Update Memory
            # ---------------------------------

            if tool_name == "search_products":

                try:

                    products = [
                        json.loads(item)
                        for item in tool_result
                    ]

                    self.memory.set_last_products(
                        products,
                    )

                    if len(products) == 1:

                        product = products[0]

                        self.memory.set_selected_product(
                            product,
                        )

                        self.memory.set_pending_order(
                            {
                                "product_id": product["id"],
                                "quantity": 1,
                            }
                        )

                        user = self.memory.get_current_user()

                        if user:

                            self.memory.set_state(
                                "ready_to_create_order"
                            )

                            return (
                                f"✅ I found one matching product.\n\n"
                                f"**{product['name']}**\n"
                                f"₹{product['price']}\n\n"
                                "Type **confirm** to place your order."
                            )

                        self.memory.set_state(
                            "waiting_phone"
                        )

                        return (
                            f"✅ I found one matching product.\n\n"
                            f"**{product['name']}**\n"
                            f"₹{product['price']}\n\n"
                            "Before placing your order,\n"
                            "please enter your phone number."
                        )

                except Exception as e:
                    print("Memory Error:", e)

            elif tool_name == "get_product":

                try:

                    product = json.loads(
                        tool_result[0]
                    )

                    self.memory.set_selected_product(
                        product,
                    )

                except Exception as e:
                    print("Memory Error:", e)

            elif tool_name == "create_user":

                try:

                    user = json.loads(
                        tool_result[0]
                    )

                    self.memory.set_current_user(
                        user,
                    )

                except Exception as e:
                    print("Memory Error:", e)

            return summarize_response(
                user_query,
                "\n".join(tool_result),
            )

        except Exception as e:
            traceback.print_exc()
            return f"Sorry, an error occurred: {e}"