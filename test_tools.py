import asyncio
from ai_assistant.mcp_client import MCPClient

async def main():
    client = MCPClient()

    tools = await client.list_tools()

    print("\nAvailable MCP Tools:\n")

    for tool in tools:
        print(tool.name)

asyncio.run(main())