import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import asyncio
from mcp.server.mcpserver import MCPServer
from database.database import SessionLocal
from database.models import Employee
from sqlalchemy import text
server = MCPServer("PostgreSQL")


@server.tool()
def get_all_employees():
    """Return all employees."""

    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                SELECT id, name, department, salary
                FROM employees
                ORDER BY id
            """)
        )

        return [tuple(row) for row in result.fetchall()]

    finally:
        db.close()


@server.tool()
def get_employee_by_id(id: int):
    """Return an employee by ID."""

    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                SELECT id, name, department, salary
                FROM employees
                WHERE id = :id
            """),
            {"id": id},
        )

        row = result.fetchone()

        return tuple(row) if row else None

    finally:
        db.close()


@server.tool()
def delete_employee(employee_id: int):
    """Delete an employee by ID."""

    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                DELETE FROM employees
                WHERE id = :employee_id
            """),
            {"employee_id": employee_id},
        )

        db.commit()

        if result.rowcount == 0:
            return f"Employee {employee_id} not found."

        return f"Employee {employee_id} deleted successfully."

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


@server.tool()
def update_employee(employee_id: int, field: str, value: str):
    """Update an employee field."""

    allowed_fields = {
        "name",
        "department",
        "salary",
    }

    field = field.lower().strip()

    if field not in allowed_fields:
        return f"'{field}' cannot be updated."

    db = SessionLocal()

    try:
        # Field name cannot be passed as a normal SQL parameter,
        # so we validate it against the allowed_fields list first.
        sql = text(f"""
            UPDATE employees
            SET {field} = :value
            WHERE id = :employee_id
        """)

        result = db.execute(
            sql,
            {
                "value": value,
                "employee_id": employee_id,
            },
        )

        db.commit()

        if result.rowcount == 0:
            return f"Employee {employee_id} not found."

        return f"{field} updated successfully for Employee {employee_id}."

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


@server.tool()
def add_employee(name: str, department: str, salary: int):
    """Add a new employee."""

    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                INSERT INTO employees(name, department, salary)
                VALUES (:name, :department, :salary)
                RETURNING id
            """),
            {
                "name": name,
                "department": department,
                "salary": salary,
            },
        )

        employee_id = result.scalar_one()

        db.commit()

        return f"Employee '{name}' added successfully with ID {employee_id}."

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())