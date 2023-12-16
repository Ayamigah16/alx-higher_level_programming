#!/usr/bin/python3
"""
Module documentation: State class definition.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the 'states' table in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
