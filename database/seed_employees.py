from database.database import SessionLocal
from database.models import Employee


employees = [
    Employee(name="John", department="Engineering", salary=90000),
    Employee(name="Alice", department="HR", salary=70000),
    Employee(name="Bob", department="Finance", salary=85000),
    Employee(name="David", department="Engineering", salary=95000),
    Employee(name="Emma", department="Marketing", salary=65000),
]


db = SessionLocal()

try:
    db.add_all(employees)
    db.commit()

    print("5 employees inserted successfully.")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()