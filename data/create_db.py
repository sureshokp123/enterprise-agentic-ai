import sqlite3

conn = sqlite3.connect("data/company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

employees = [
    ("John", "Engineering", 90000),
    ("Alice", "HR", 70000),
    ("Bob", "Finance", 85000),
    ("David", "Engineering", 95000),
    ("Emma", "Marketing", 65000),
]

cursor.executemany(
    """
    INSERT INTO employees(name, department, salary)
    VALUES(?,?,?)
    """,
    employees,
)

conn.commit()
conn.close()

print("Database Created Successfully")