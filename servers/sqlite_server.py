import asyncio
import sqlite3

from mcp.server.mcpserver import MCPServer

server = MCPServer("SQLite")


@server.tool()
def get_all_employees():

    conn = sqlite3.connect("data/company.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM employees
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


@server.tool()
def get_employee_by_id(id: int):

    conn = sqlite3.connect("data/company.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM employees
        WHERE id=?
        """,
        (id,),
    )

    row = cursor.fetchone()

    conn.close()

    return row


if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())