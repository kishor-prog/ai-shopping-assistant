from mcp.server.fastmcp import FastMCP

from mcp_server.api_client import api_client

#this function is used to register the category tools in the MCP server
def register_category_tools(mcp: FastMCP):

    @mcp.tool()
    def list_categories():
        """List all categories."""

        return api_client.get("/categories/")

    @mcp.tool()
    def get_category(category_id: int):
        """Get a category by its ID."""

        return api_client.get(
            f"/categories/{category_id}"
        )