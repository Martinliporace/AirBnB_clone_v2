#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Amenity(BaseModel, Base):
    """Amenities"""
    __tablename__ = 'amenities'
