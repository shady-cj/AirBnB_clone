#!/usr/bin/python3
"""
This module defines a model for cities
which is mapped to the state in which they are
while inheriting from BaseModel
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Defining City class and defining
    placeholder variable
    state_id to hold the id of the state in which
    they belong and the name of the city
    """
    name = ""
    state_id = ""
