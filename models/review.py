#!/usr/bin/python3
"""
This module defines a model for reviews
by users for each place
while inheriting from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Defining Review class and defining
    placeholder variable
    """
    place_id = ""
    user_id = ""
    text = ""
