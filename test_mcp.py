import asyncio

from ai_assistant.mcp_client import MCPClient


async def main():
    client = MCPClient()

    tools = await client.list_tools()

    for tool in tools:
        print("=" * 60)
        print(tool.name)
        print(tool.inputSchema)
        print("=" * 60)


asyncio.run(main())