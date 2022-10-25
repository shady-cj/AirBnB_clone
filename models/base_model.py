#!/usr/bin/python3
"""
This module contains a the BaseModel() class that serves as the base
for which other models in this project will inherit from
"""
import uuid
import datetime


class BaseModel:
    """ Defining the base class for all other models """

    def __init__(self):
        """ Instantiation of instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        This allows for creating a user friendly info
        of the instance
        """
        return f"[{type(self).__name__}] ({self.id}) \
{self.__dict__}"

    def save(self):
        """ This creates a save method that updates
        the instance attributes
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        A method to create a dict off an instance for serialization
        """
        instance_dict = dict(self.__dict__)
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        return instance_dict
