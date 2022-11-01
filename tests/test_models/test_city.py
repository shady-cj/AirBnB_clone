#!/usr/bin/python3
"""
This module writes tests for City model
"""
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage
import unittest


class TestState(unittest.TestCase):
    def test_city_creation(self):
        """Testing city creation"""
        city = City()
        state = State()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        city.state_id = state.id
        city.name = "test city"
        self.assertEqual(city.name, "test city")
        self.assertEqual(city.state_id, state.id)
        self.assertIsInstance(city.id, str)

    def test_city_dict_to_instance(self):
        """Testing city conversion from dict to instance object"""
        city = City()
        state = State()
        city.name = "Test"
        city.state_id = state.id
        self.assertIsInstance(city.to_dict(), dict)
        self.assertEqual(city.to_dict()["__class__"], "City")
        new_city = City(**city.to_dict())
        self.assertNotEqual(city, new_city)
        self.assertEqual(city.id, new_city.id)
        self.assertEqual(city.state_id, new_city.state_id)

    def test_city_storage(self):
        """ Test City Storage """
        ct = City()
        storage = FileStorage()
        get_obj = storage.all().get(f"City.{ct.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, ct.id)
        ct.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"City.{ct.id}"))
        self.assertIsInstance(s2.get(f"City.{ct.id}"), City)
        self.assertEqual(s2.get(f"City.{ct.id}").created_at, ct.created_at)
