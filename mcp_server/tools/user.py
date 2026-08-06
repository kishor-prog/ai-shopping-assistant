from mcp.server.fastmcp import FastMCP

from mcp_server.api_client import api_client

#this function is used to register the user tools in the MCP server
def register_user_tools(mcp: FastMCP):

    @mcp.tool()
    def create_user(
        name: str,
        email: str,
        phone: str,
    ):
        """
        Register a new user.
        """

        return api_client.post(
            "/users/",
            json={
                "name": name,
                "email": email,
                "phone": phone,
            },
        )

    @mcp.tool()
    def list_users():
        """
        List all users.
        """

        return api_client.get("/users/")

    @mcp.tool()
    def get_user(user_id: int):
        """
        Get a user by its ID.
        """

        return api_client.get(
            f"/users/{user_id}"
        )

    @mcp.tool()
    def get_user_by_phone(
    phone: str,
  ):
      """
      Get a user by phone number.
      """

      return api_client.get(
        f"/users/phone/{phone}"
       )