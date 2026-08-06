from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

#turns on the MCP client sever to execute tools from the mcp_server/server.py file
class MCPClient:

    def __init__(self):

        self.server_params = StdioServerParameters(
            command="python",
            args=["mcp_server/server.py"],
        )

#this function creates a session with the MCP server and initializes it
    async def _create_session(self):
        """
        Create and initialize an MCP session.
        """

        read, write = await stdio_client(
            self.server_params
        ).__aenter__()

        session = ClientSession(read, write)

        await session.__aenter__()

        await session.initialize()

        return session, read, write
    
#this function lists all the registered tools in MCP server
    async def list_tools(self):
        """
        Return all registered MCP tools.
        """

        async with stdio_client(self.server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.list_tools()

                return result.tools
            
#this function executes a tool from MCP server with the given tool name and arguments and return it
    async def execute(
        self,
        tool_name: str,
        arguments: dict | None = None,
    ):
        """
        Execute an MCP Tool.
        """

        if arguments is None:
            arguments = {}

        try:

            async with stdio_client(self.server_params) as (read, write):

                async with ClientSession(read, write) as session:

                    await session.initialize()

                    print("=" * 60)
                    print("MCP SERVER")
                    print(f"Executing Tool : {tool_name}")
                    print(f"Arguments      : {arguments}")
                    print("=" * 60)

                    result = await session.call_tool(
                        tool_name,
                        arguments,
                    )

                    if result.isError:
                        raise Exception(
                            result.content[0].text
                        )

                    return [
                        item.text
                        for item in result.content
                    ]

        except Exception as e:

            print("\n" + "=" * 60)
            print("MCP ERROR")
            print("Exception Type :", type(e))
            print("Exception      :", e)
            print("=" * 60 + "\n")

            raise