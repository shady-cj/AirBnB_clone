#!/usr/bin/python3
"""
This module writes tests for Place model
"""
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import unittest


class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        """Testing place creation"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        city = City()
        user = User()
        name = "Test name"
        description = "Test description"
        number_rooms = 4
        number_bathrooms = 4
        max_guest = 6
        price_by_night = 2200
        latitude = 3.13
        longitude = 43.12
        am1 = Amenity()
        am2 = Amenity()
        am3 = Amenity()
        am = [am1.id, am2.id, am3.id]
        place.city_id = city.id
        place.user_id = user.id
        place.name = name
        place.description = description
        place.number_rooms = number_rooms
        place.number_bathrooms = number_bathrooms
        place.max_guest = max_guest
        place.price_by_night = price_by_night
        place.latitude = latitude
        place.longitude = longitude
        place.amenity_ids.extend(am)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.name, name)
        self.assertEqual(place.description, description)
        self.assertEqual(place.number_rooms, number_rooms)
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        self.assertEqual(place.max_guest, max_guest)
        self.assertEqual(place.price_by_night, price_by_night)
        self.assertEqual(place.latitude, latitude)
        self.assertEqual(place.longitude, longitude)
        self.assertEqual(place.amenity_ids, am)
        self.assertIsInstance(place.id, str)

    def test_place_dict_to_instance(self):
        """Testing place conversion from dict to instance object"""
        place = Place()
        self.assertIsInstance(place.to_dict(), dict)
        self.assertEqual(place.to_dict()["__class__"], "Place")
        new_place = Place(**place.to_dict())
        self.assertNotEqual(place, new_place)
        self.assertEqual(place.id, new_place.id)
        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(place.updated_at, new_place.updated_at)
    
    def test_place_storage(self):
        """ Test Place Storage """
        pl = Place()
        storage = FileStorage()
        get_obj = storage.all().get(f"Place.{pl.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, pl.id)
        pl.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"Place.{pl.id}"))
        self.assertIsInstance(s2.get(f"Place.{pl.id}"), Place)
        self.assertEqual(s2.get(f"Place.{pl.id}").created_at, pl.created_at)
