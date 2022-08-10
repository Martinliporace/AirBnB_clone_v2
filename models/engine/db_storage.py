#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone """

import models
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from models.user import User
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """Class DB"""
    __engine = None
    __session = None

    def __init__(self):
        """ Class constructor  """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all objects
        depending of the class name (argument cls) """

        new_dict = {}
        if cls is None:
            for k, value in classes.items():
                for clase in self.__session.query(value).all():
                    key = "{}.{}".format(k, clase.id)
                    new_dict[key] = clase
        else:
            for clase in self.__session.query(classes[cls]).all():
                key = "{}.{}".format(cls, clase.id)
                new_dict[key] = clase

        return new_dict

    def new(self, obj):
        """ add the object to the current database session (self.__session) """

        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session
        (self.__session) """

        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) (WARNING:
        all classes who inherit from Base must be imported before calling
        Base.metadata.create_all(engine)) create the current database
        session (self.__session) from the engine (self.__engine) by using a
        sessionmaker - the option expire_on_commit must be set to False ; and
        scoped_session - to make sure your Session is thread-safe """

        Base.metadata.create_all(self.__engine)
        temp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(temp)
        self.__session = Session()

    def close(self):
        """closes session"""
        self.__session.close()
