from mcp.server.mcpserver import MCPServer

import asyncio

server = MCPServer("Calculator")


@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@server.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())
