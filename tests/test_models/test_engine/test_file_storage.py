#!/usr/bin/python3
"""
This module write testcases for file_storage.py
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.user import User
import os
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """
    Testing FileStorage class and its functionality
    """

    def setUp(self):
        self.user1 = User()
        self.user1.email = "example@gmail.com"
        self.user1.first_name = "John"
        self.user1.last_name = "Doe"
        self.state1 = State()
        self.state1.name = "Test state"

    def test_objects_presence(self):
        """
        Testing objects persistence before and after
        saving
        """
        storage = FileStorage()
        self.assertIsNotNone(storage.all().get(f"User.{self.user1.id}"))
        self.assertIsNotNone(storage.all().get(f"State.{self.state1.id}"))

    def test_objects_not_saved_only_if_save_is_called(self):
        """
        Tests that the instance are not saved to file until the
        save method is called
        """
        with open("file.json") as f:
            obj = json.load(f)
            self.assertIsNone(obj.get(f"User.{self.user1.id}"))
            self.assertIsNone(obj.get(f"State.{self.state1.id}"))

    def test_objects_saved_when_save_method_is_called(self):
        """
        Tests that the instance are saved to file if save method is called
        """
        self.user1.save()
        self.state1.save()
        with open("file.json") as f:
            obj = json.load(f)
            self.assertIsNotNone(obj.get(f"User.{self.user1.id}"))
            self.assertIsNotNone(obj.get(f"State.{self.state1.id}"))
