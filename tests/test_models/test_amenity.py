#!/usr/bin/python3
"""
This module writes tests for Amenity model
"""
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import unittest


class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        """Testing amenity creation"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Test"
        self.assertEqual(amenity.name, "Test")
        self.assertIsInstance(amenity.id, str)

    def test_amenity_dict_to_instance(self):
        """Testing amenity conversion from dict to instance object"""
        amenity = Amenity()
        amenity.name = "Test"
        self.assertIsInstance(amenity.to_dict(), dict)
        self.assertEqual(amenity.to_dict()["__class__"], "Amenity")
        new_amenity = Amenity(**amenity.to_dict())
        self.assertNotEqual(amenity, new_amenity)
        self.assertEqual(amenity.id, new_amenity.id)
        self.assertEqual(amenity.name, new_amenity.name)

    def test_amenity_storage(self):
        """ Test Amenity Storage """
        am = Amenity()
        storage = FileStorage()
        get_obj = storage.all().get(f"Amenity.{am.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, am.id)
        am.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"Amenity.{am.id}"))
        self.assertIsInstance(s2.get(f"Amenity.{am.id}"), Amenity)
        self.assertEqual(s2.get(f"Amenity.{am.id}").created_at, am.created_at)
