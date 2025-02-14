#!/usr/bin/python3
"""This module defines a class User"""
import sqlalchemy
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import models
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.storage_t == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
