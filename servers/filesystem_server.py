import asyncio
from pathlib import Path

from mcp.server.mcpserver import MCPServer

server = MCPServer("Filesystem")


@server.tool()
def read_file(filename: str) -> str:
    """
    Read a file from the data folder.
    """

    data_folder = Path("data")

    file_path = data_folder / filename

    if not file_path.exists():
        return f"File '{filename}' not found."

    return file_path.read_text(encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())