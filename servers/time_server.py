from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Time")


@mcp.tool()
def get_time() -> str:
    return str(datetime.now())


if __name__ == "__main__":
    mcp.run()