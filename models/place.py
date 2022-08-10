#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from models import storage
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

if (models.type_storage == "db"):
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


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
        amenity_ids = []

        @property
        def reviews(self):
            """Lists all reviews"""
            new_dict = self.reviews
            reviews_list = []
            for key, value in new_dict.items():
                if self.id == value.review_id:
                    reviews_list.append(value)

            return reviews_list

        @property
        def amenities(self):
            """Lists all amenities"""
            new_dict = self.amenities
            amenities_list = []
            for key, value in new_dict.items():
                if self.id == value.amenities_id:
                    amenities_list.append(value)

            return amenities_list

        @amenities.setter
        def amenities(self, amenities=None):
            """ Amenities setter"""
            if type(amenities) == Amenity:
                new_list = []
                self.new_list.append(amenities.id)
