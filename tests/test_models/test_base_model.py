#!/usr/bin/python3
"""
This model Tests the BaseModel class using unittest
"""
import unittest
from models.base_model import BaseModel
import uuid
import datetime
import time
from models.engine.file_storage import FileStorage
import os
import json


class TestBaseModelBasic(unittest.TestCase):
    """ Testing for basic attributes and methods on
    BaseModel instantiation
    """
    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_id(self):
        """ Testing if id was assigned to each Instance
        and it's a uuid generated id
        """
        self.assertIsInstance(self.b1.id, str)
        u = uuid.UUID(self.b1.id)
        self.assertIsInstance(u, uuid.UUID)
        self.assertEqual(u.version, 4)

    def test_timestamp(self):
        """
        Testing the created_at and updated_at timestamp
        """
        self.assertIsInstance(self.b1.created_at, datetime.datetime)
        self.assertIsInstance(self.b2.created_at, datetime.datetime)
        self.assertIsInstance(self.b1.updated_at, datetime.datetime)
        self.assertIsInstance(self.b2.updated_at, datetime.datetime)

    def test_str_method(self):
        """
        Testing the str method of the instance
        """
        expected_rep_b1 = f"[{self.b1.__class__.__name__}] \
({self.b1.id}) {self.b1.__dict__}"
        expected_rep_b2 = f"[{self.b2.__class__.__name__}] \
({self.b2.id}) {self.b2.__dict__}"
        self.assertEqual(str(self.b1), expected_rep_b1)
        self.assertEqual(str(self.b2), expected_rep_b2)

    def test_save_method_basic(self):
        """
        Test if save() method updates the updated_at field
        """
        time.sleep(2)
        n = datetime.datetime.now()
        self.b1.save()
        self.assertNotEqual(self.b1.updated_at, self.b1.created_at)
        self.assertEqual(self.b1.updated_at.second, n.second)
        self.assertEqual(self.b1.updated_at.minute, n.minute)

    def test_to_dict(self):
        """
        Test on the to_dict() method
        """
        b1_dict = dict(self.b1.__dict__)
        b2_dict = dict(self.b2.__dict__)
        self.assertNotEqual(b1_dict, self.b1.to_dict())
        self.assertNotEqual(b2_dict, self.b2.to_dict())

        b1_dict["__class__"] = type(self.b1).__name__
        b2_dict["__class__"] = type(self.b2).__name__
        b2_dict["created_at"] = b2_dict["created_at"].isoformat()
        b2_dict["updated_at"] = b2_dict["updated_at"].isoformat()
        b1_dict["created_at"] = b1_dict["created_at"].isoformat()
        b1_dict["updated_at"] = b1_dict["updated_at"].isoformat()
        self.assertEqual(b1_dict, self.b1.to_dict())
        self.assertEqual(b2_dict, self.b2.to_dict())


class TestBaseModelCreation(unittest.TestCase):
    """
    This Testcase tests the BaseModel class for the
    creation of new instances from a dictionary
    """
    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_creation_with_dict(self):
        """
        This creates a new BaseModel instance from a valid dict
        """
        new_b1 = BaseModel(**self.b1.to_dict())
        new_b2 = BaseModel(**self.b2.to_dict())
        self.assertNotEqual(new_b1, self.b1)
        self.assertNotEqual(new_b2, self.b2)
        self.assertEqual(self.b2.id, new_b2.id)
        self.assertEqual(self.b1.id, new_b1.id)
        self.assertEqual(self.b1.created_at, new_b1.created_at)
        self.assertEqual(self.b2.created_at, new_b2.created_at)
        self.assertEqual(self.b1.updated_at, new_b1.updated_at)
        self.assertEqual(self.b2.updated_at, new_b2.updated_at)

    def test_creation_with_empty_dict(self):
        """
        Testing if the dict to create the instance with is empty
        """
        new_b1 = BaseModel(**{})
        self.assertNotEqual(new_b1.__dict__, 0)
        self.assertIsNotNone(getattr(new_b1, "id", None))

    def test_creation_with_invalid_dict(self):
        """
        Testing the instance with invalid dict
        """
        new_b1 = BaseModel(self.b1)

        self.assertNotEqual(new_b1.__dict__, 0)
        self.assertIsNotNone(getattr(new_b1, "id", None))

        with self.assertRaises(TypeError):
            BaseModel(**self.b1)


class TestBaseModelFileStorage(unittest.TestCase):
    """
    Testing storage of instances using local files
    """
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    @classmethod
    def setUpClass(cls):
        cls.b = BaseModel()

    def test_file_save_after_instance_creation(self):
        """
        Test if the data is stored somewhere after instantiating
        a model class
        """
        new_b = BaseModel(**self.b.to_dict())
        self.storage.new(new_b)
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(
            self.storage.all()[f"BaseModel.{self.b.id}"]["id"], self.b.id)
        new_b.save()

    def test_instance_data_persistence_after_save(self):
        """Test if there is data persistence after saving"""
        self.assertTrue(self.storage.all()[f"BaseModel.{self.b.id}"]["id"])
        self.assertEqual(
            self.storage.all()[f"BaseModel.{self.b.id}"]["id"], self.b.id)
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as f:
            reader = json.load(f)
            self.assertIsNotNone(reader.get(f"BaseModel.{self.b.id}"))
