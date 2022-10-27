#!/usr/bin/python3
"""
This module defines a model for the Amenities
in a place while inheriting from BaseModel
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Defining Amenity class and defining
    placeholder variable
    """
    name = ""
