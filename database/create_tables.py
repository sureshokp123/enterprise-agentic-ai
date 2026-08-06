from database.database import Base, engine
from database.models import Employee

Base.metadata.create_all(bind=engine)

print("Tables created successfully")