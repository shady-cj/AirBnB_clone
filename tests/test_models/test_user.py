#!/usr/bin/python3
"""
This module writes tests for User model
"""
from models.user import User
from models.engine.file_storage import FileStorage
import unittest


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Testing user creation"""
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.last_name, "")
        User.first_name = "John"
        User.last_name = "Doe"
        User.password = "123"
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.password, "123")
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

    def test_user_storage(self):
        """ Test User Storage """
        u = User()
        storage = FileStorage()
        get_obj = storage.all().get(f"User.{u.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, u.id)
        u.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"User.{u.id}"))
        self.assertIsInstance(s2.get(f"User.{u.id}"), User)
        self.assertEqual(s2.get(f"User.{u.id}").created_at, u.created_at)
