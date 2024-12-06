from app.backend.db import Base
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from task import Task


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, index=True)
    user = relationship("Task", back_populates="user")


print(CreateTable(User.__table__))