import asyncio
from client.mcp_client import MCPClient


async def main():

    client = MCPClient()

    result = await client.call_tool(
        "add",
        {
            "a": 100,
            "b": 200
        }
    )

    print(result)


asyncio.run(main())