import asyncio

from ai_assistant.mcp_client import MCPClient
from ai_assistant.tool_manager import convert_mcp_tools


async def main():
    client = MCPClient()

    mcp_tools = await client.list_tools()

    gemini_tools = convert_mcp_tools(mcp_tools)

    for tool in gemini_tools:
        print("=" * 50)
        print(tool.name)
        print(tool.description)
        print(tool.parameters)


if __name__ == "__main__":
    asyncio.run(main())