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

@server.tool()
def delete_employee(employee_id: int):

    """
    Delete an employee by ID.
    """

    conn = sqlite3.connect("data/company.db")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    if deleted == 0:
        return f"Employee {employee_id} not found."

    return f"Employee {employee_id} deleted successfully."

@server.tool()
def update_employee(employee_id: int, field: str, value: str):
    """
    Update allowed employee fields.
    """

    allowed_fields = [
        "name",
        "department",
        "salary"
    ]

    if field.lower() not in allowed_fields:
        return f"'{field}' cannot be updated."

    conn = sqlite3.connect("data/company.db")

    cursor = conn.cursor()

    sql = f"""
        UPDATE employees
        SET {field} = ?
        WHERE id = ?
    """

    cursor.execute(sql, (value, employee_id))

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    if updated == 0:
        return f"Employee {employee_id} not found."

    return f"{field} updated successfully for Employee {employee_id}."

@server.tool()
def add_employee(name: str, department: str, salary: int):
    """
    Add a new employee.
    """

    conn = sqlite3.connect("data/company.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO employees(name, department, salary)
        VALUES (?, ?, ?)
        """,
        (name, department, salary)
    )

    conn.commit()

    employee_id = cursor.lastrowid

    conn.close()

    return f"Employee '{name}' added successfully with ID {employee_id}."

if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())