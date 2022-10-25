#!/usr/bin/python3
"""
This module provides a FileStorage class that serializes
anf deserializes instances from/to json file
"""
import json
import os


class FileStorage:
    """ Creating the file storage and its private attributes """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the dict __objects
        """
        return self.__objects

    def new(self, obj):
        """ Sets the new obj in the __objects store
        """
        obj_key = f"{type(obj).__name__}.{obj.id}"
        self.__class__.__objects[obj_key] = obj.to_dict()

    def save(self):
        """
        This serializes __objects into file <__file_path>
        """
        with open(self.__file_path, "w") as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """
        This method deserializes from the file __file_path if
        __file_path exists and stores into __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as fp:
                self.__objects = json.load(fp)
