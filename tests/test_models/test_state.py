#!/usr/bin/python3
"""
This module writes tests for State model
"""
from models.state import State
from models.engine.file_storage import FileStorage
import unittest


class TestState(unittest.TestCase):
    def test_state_creation(self):
        """Testing state creation"""
        state = State()
        self.assertEqual(state.name, "")
        state.name = "Example"
        self.assertEqual(state.name, "Example")
        self.assertIsInstance(state.id, str)

    def test_state_dict_to_instance(self):
        """Testing state conversion from dict to instance object"""
        state = State()
        state.name = "LA"
        self.assertIsInstance(state.to_dict(), dict)
        self.assertEqual(state.to_dict()["__class__"], "State")
        new_state = State(**state.to_dict())
        self.assertNotEqual(state, new_state)
        self.assertEqual(state.id, new_state.id)
        self.assertEqual(state.name, new_state.name)

    def test_state_storage(self):
        """ Test State Storage """
        st = State()
        storage = FileStorage()
        get_obj = storage.all().get(f"State.{st.id}")
        self.assertIsNotNone(get_obj)
        self.assertEqual(get_obj.id, st.id)
        st.save()
        s2 = FileStorage()
        s2.reload()
        s2 = s2.all()
        self.assertIsNotNone(s2.get(f"State.{st.id}"))
        self.assertIsInstance(s2.get(f"State.{st.id}"), State)
        self.assertEqual(s2.get(f"State.{st.id}").created_at, st.created_at)
