import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

TOOL_SERVER_MAP = {
    "add": "servers/calculator_server.py",
    "multiply": "servers/calculator_server.py",
    "read_file": "servers/filesystem_server.py",

    "get_all_employees": "servers/sqlite_server.py",
    "get_employee_by_id": "servers/sqlite_server.py",
    "delete_employee": "servers/sqlite_server.py",
    "update_employee": "servers/sqlite_server.py",
    "add_employee": "servers/sqlite_server.py",
}

class MCPClient:

    async def call_tool(self, tool_name: str, arguments: dict):

        if tool_name not in TOOL_SERVER_MAP:
            raise Exception(f"Unknown tool: {tool_name}")

        server = TOOL_SERVER_MAP[tool_name]

        server_params = StdioServerParameters(
            command="python",
            args=[server],
        )

        async with stdio_client(server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                return await session.call_tool(
                    tool_name,
                    arguments,
                )