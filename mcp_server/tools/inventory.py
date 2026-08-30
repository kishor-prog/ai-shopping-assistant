from mcp.server.fastmcp import FastMCP
from mcp_server.api_client import api_client


def register_inventory_tools(mcp: FastMCP):

    @mcp.tool()
    def list_inventory():
        """
        List all inventory records across warehouses.
        """
        return api_client.get("/inventory/")

    @mcp.tool()
    def get_inventory(inventory_id: int):
        """
        Get inventory details by inventory ID.
        """
        return api_client.get(f"/inventory/{inventory_id}")
