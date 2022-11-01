#!/usr/bin/python3
"""
Testcases for console.py cmd prompt
"""
from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import json


class TestConsoleBasicCommand(unittest.TestCase):

    def test_quit(self):
        """ test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')
            self.assertTrue(HBNBCommand().do_quit("quit"))

    def test_EOF(self):
        """ Test EOF """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')
            self.assertTrue(HBNBCommand().do_EOF("EOF"))

    def test_help(self):
        """Testing the help commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = "\n".join([
            "",
            "Documented commands (type help <topic>):",
            "========================================",
            "EOF  all  create  destroy  help  quit  show  update",
            "\n"
            ])
            self.assertEqual(f.getvalue(), output)

    def test_emptyline(self):
        """ Testing emptyline """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), '')
            HBNBCommand().onecmd("        ")
            self.assertEqual(f.getvalue(), '')


class TestCreateCommand(unittest.TestCase):
    def test_base_model(self):
        """Test create on basemodel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            value = f.getvalue().strip("\n")
            self.assertIsInstance(value, str)
            with open("file.json") as fp:
                reader = json.load(fp)
                self.assertIsNotNone(reader.get(f"BaseModel.{value}"))
                self.assertIsNotNone(
                        reader.get(f"BaseModel.{value}")["__class__"] == "BaseModel")
    def test_user(self):
        """Test create on basemodel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            value = f.getvalue().strip("\n")
            self.assertIsInstance(value, str)
            with open("file.json") as fp:
                reader = json.load(fp)
                self.assertIsNotNone(reader.get(f"User.{value}"))
                self.assertIsNotNone(
                        reader.get(f"User.{value}")["__class__"] == "BaseModel")


class TestAllCommand(unittest.TestCase):
    def test_all_plain(self):
        """ Test all command without any other args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                self.assertEqual(len(r), len(value))

    def test_all_base_model_plain(self):
        """ Test all on basemodel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("BaseModel"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_user_plain(self):
        """ Test all on user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("User"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_place_plain(self):
        """ Test all on place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Place"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_city_plain(self):
        """ Test all on city """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("City"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_amenities_plain(self):
        """ Test all on amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Amenity"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_review_plain(self):
        """ Test all on review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Review"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_state_plain(self):
        """ Test all on state """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("State"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_base_model(self):
        """ Test all on basemodel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("BaseModel"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_user(self):
        """ Test all on user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("User"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_place(self):
        """ Test all on place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Place"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_city(self):
        """ Test all on city """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("City"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_amenities(self):
        """ Test all on amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Amenity"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_review(self):
        """ Test all on review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("Review"):
                        count += 1
                self.assertEqual(count, len(value))

    def test_all_state(self):
        """ Test all on state """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            value = eval(f.getvalue().strip("\n"))
            self.assertIsInstance(value, list)
            with open("file.json") as fp:
                r = json.load(fp)
                count = 0
                for k in r.keys():
                    if k.startswith("State"):
                        count += 1
                self.assertEqual(count, len(value))
