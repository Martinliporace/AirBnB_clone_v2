#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from models import storage
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if (models.type_storage == "db"):
        city_id = Column(String(60),  ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)


        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)

    else:

        @property
        def reviews(self):
            """ returns the list of Review instances with place_id
            equals to the current Place.id"""

            reviews_list = []
            new_dict = storage.all(self)
            for key, value in new_dict.items():
                if value.place_id == self.id:
                    reviews_list.append(new_dict[key])
            return reviews_list

        @property
        def amenities(self):
            """  returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place """

            return self.amenities

        @amenities.setter
        def amenities_setter(self, amenities=None):
            """setter of amenities"""
            if type(amenities) == Amenity:
                am_list = []
                self.am_ist.append(amenities.id)


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))

