#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.place import Place
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
#    if (models.type_storage == "db"):
#        places = relationship(Place, backref="cities")
