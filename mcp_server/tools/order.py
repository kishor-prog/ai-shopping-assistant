from mcp.server.fastmcp import FastMCP

from mcp_server.api_client import api_client

#this function is used to register the order tools in the MCP server
def register_order_tools(mcp: FastMCP):

    @mcp.tool()
    def create_order(
        user_id: int,
        product_id: int,
        quantity: int,
    ):
        """
        Create a new order.
        """

        return api_client.post(
            "/orders/",
            json={
                "user_id": user_id,
                "product_id": product_id,
                "quantity": quantity,
            },
        )

    @mcp.tool()
    def list_orders():
        """
        List all orders.
        """

        return api_client.get("/orders/")

    @mcp.tool()
    def get_order(order_id: int):
        """
        Get an order by ID.
        """

        return api_client.get(
            f"/orders/{order_id}"
        )