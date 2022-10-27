#!/usr/bin/python3
"""
This module defines a model for states
while inheriting from BaseModel
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    Defining State class and defining
    placeholder variable
    """
    name = ""
