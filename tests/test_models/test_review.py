#!/usr/bin/python3
"""
This module writes tests for Review model
"""
from models.review import Review
from models.place import Place
from models.user import User
from models.engine.file_storage import FileStorage
import unittest


class TestReview(unittest.TestCase):
    def test_review_creation(self):
        """Testing review creation"""
        review = Review()
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")
        user = User()
        place = Place()
        review.user_id = user.id
        review.place_id = place.id
        review.text = "Test text"
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.text, "Test text")
        self.assertIsInstance(review.id, str)

    def test_review_dict_to_instance(self):
        """Testing review conversion from dict to instance object"""
        review = Review()
        user = User()
        place = Place()
        review.user_id = user.id
        review.place_id = place.id
        self.assertIsInstance(review.to_dict(), dict)
        self.assertTrue(review.to_dict().get("user_id"))
        self.assertTrue(review.to_dict().get("place_id"))
        self.assertEqual(review.to_dict()["__class__"], "Review")
        new_review = Review(**review.to_dict())
        self.assertNotEqual(review, new_review)
        self.assertEqual(review.id, new_review.id)
        self.assertEqual(review.user_id, new_review.user_id)
        self.assertEqual(review.place_id, new_review.place_id)

    def test_review_storage(self):
        """ Test Review Storage """
        rv = Review()
        storage = FileStorage()
        get_obj = storage.all().get(f"Review.{rv.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, rv.id)
        rv.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"Review.{rv.id}"))
        self.assertIsInstance(s2.get(f"Review.{rv.id}"), Review)
        self.assertEqual(s2.get(f"Review.{rv.id}").created_at, rv.created_at)
