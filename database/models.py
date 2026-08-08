from database.database import Base
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String, Text

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Integer)


class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    category = Column(String)

    chunk_id = Column(Integer)

    content = Column(Text)

    embedding = Column(Vector(1536))