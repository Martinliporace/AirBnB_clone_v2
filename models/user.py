#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user")

        reviews = relationship("Review", backref="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = ""
        review = ""
