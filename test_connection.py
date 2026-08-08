# from sqlalchemy import create_engine, text
# # from config import DATABASE_URL

# engine = create_engine("postgresql://postgres:Sureshokp1205@localhost:5432/enterprise_agentic_ai")

# with engine.connect() as conn:
#     print("Database:", conn.execute(text("SELECT current_database()")).scalar())
#     print("Extensions:", conn.execute(text("SELECT extname FROM pg_extension")).fetchall())

from sqlalchemy import create_engine, text
# from config import DATABASE_URL

engine = create_engine("postgresql://postgres:Sureshokp1205@localhost:5432/enterprise_agentic_ai")

with engine.connect() as conn:
    print("=" * 50)

    print("Current Database:")
    print(conn.execute(text("SELECT current_database();")).fetchall())

    print("\nCurrent User:")
    print(conn.execute(text("SELECT current_user;")).fetchall())

    print("\nCurrent Port:")
    print(conn.execute(text("SHOW port;")).fetchall())

    print("\nCurrent Data Directory:")
    print(conn.execute(text("SHOW data_directory;")).fetchall())

    print("\nExtensions:")
    print(conn.execute(text("SELECT extname FROM pg_extension;")).fetchall())

    print("=" * 50)