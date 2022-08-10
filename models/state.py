#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__='states'
    name = Column(String(128), nullable=False)
    if (models.type_storage == "db"):
        cities = relationship("City", backref="state")
    else:
        def cities(self):
            """represent a relationship with the class City"""
            list_cities = []
            dict_cities = models.storage.all(City)
            for city in dict_cities.values():
                if self.id == city.state_id:
                    list_cities.append(city)
            return list_cities