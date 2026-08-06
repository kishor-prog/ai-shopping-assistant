import asyncio

from ai_assistant.mcp_client import MCPClient


async def main():
    client = MCPClient()

    result = await client.execute(
        "create_user",
        {
            "name": "sham",
            "email": "sham1@example.com",
            "phone": "9876543210",
        },
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())