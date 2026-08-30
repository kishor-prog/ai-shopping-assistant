from pathlib import Path
import sys

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from mcp.server.fastmcp import FastMCP

from mcp_server.tools.product import register_product_tools
from mcp_server.tools.category import register_category_tools
from mcp_server.tools.inventory import register_inventory_tools
from mcp_server.tools.user import register_user_tools
from mcp_server.tools.order import register_order_tools

mcp = FastMCP("Ecommerce Backend MCP")

register_product_tools(mcp)
register_category_tools(mcp)
register_inventory_tools(mcp)
register_user_tools(mcp)
register_order_tools(mcp)

if __name__ == "__main__":
    mcp.run()