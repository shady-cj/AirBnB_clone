#!/usr/bin/python3
"""
This module defines a model for each place
which is mapped to the state and city in which they
are while inheriting from BaseModel
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Defining Place class and defining
    placeholder variable
    city_id to hold the id of the city in which
    they belong
    user_id The user id
    amenity_ids contains the list of the amenities
    """
    name = ""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
