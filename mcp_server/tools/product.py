from mcp.server.fastmcp import FastMCP

from mcp_server.api_client import api_client

#this function is used to register the product tools in the MCP server
def register_product_tools(mcp: FastMCP):

    @mcp.tool()
    def list_products():
        """List all products."""

        return api_client.get("/products/")

    @mcp.tool()
    def get_product(product_id: int):
        """Get product by id."""

        return api_client.get(
            f"/products/{product_id}"
        )

    @mcp.tool()
    def search_products(
        keyword: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
    ):
        """Search products."""

        params = {}

        if keyword is not None:
            params["keyword"] = keyword

        if min_price is not None:
            params["min_price"] = min_price

        if max_price is not None:
            params["max_price"] = max_price

        return api_client.get(
            "/products/search",
            params=params,
        )