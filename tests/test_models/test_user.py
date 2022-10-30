#!/usr/bin/python3
"""
This module writes tests for User model
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Testing user creation"""
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.email, "")
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertIsInstance(user.id, str)

    def test_user_dict_to_instance(self):
        """Testing user conversion from dict to instance object"""
        user = User()
        user.first_name = "John"
        user.last_name = "Doe"
        user.email = "example@example.com"
        user.password = "abc234"
        self.assertIsInstance(user.to_dict(), dict)
        self.assertEqual(user.to_dict()["__class__"], "User")
        new_user = User(**user.to_dict())
        self.assertNotEqual(user, new_user)
        self.assertEqual(user.id, new_user.id)
        self.assertEqual(user.password, new_user.password)
