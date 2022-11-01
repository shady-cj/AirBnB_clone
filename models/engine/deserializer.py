#!/usr/bin/python3
"""
A module that provides an object_hook for deserializing from
storage
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


def to_model(dct):
    if "__class__" in dct:
        class_name = dct.get("__class__")
        obj = eval(class_name)(**dct)
        return obj
    return dct
