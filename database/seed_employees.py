from database.database import SessionLocal
from database.models import Employee


def seed_employees():
    db = SessionLocal()

    try:
        existing_count = db.query(Employee).count()

        if existing_count > 0:
            print(f"Employees already exist: {existing_count}")
            return

        employees = [
            Employee(name="John", department="Engineering", salary=90000),
            Employee(name="Alice", department="HR", salary=70000),
            Employee(name="Bob", department="Finance", salary=85000),
            Employee(name="David", department="Engineering", salary=95000),
            Employee(name="Emma", department="Marketing", salary=65000),
        ]

        db.add_all(employees)
        db.commit()

        print("5 employees inserted successfully.")

    finally:
        db.close()