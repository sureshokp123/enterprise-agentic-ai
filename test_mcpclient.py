from client.mcp_client import MCPClient
import asyncio

async def main():
    client = MCPClient()

    result = await client.call_tool(
        "get_all_employees",
        {}
    )

    print(result)

asyncio.run(main())