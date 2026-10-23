from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Snippet(Base):
    __tablename__ = "snippets"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True)
    title = Column(String)
    code = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")