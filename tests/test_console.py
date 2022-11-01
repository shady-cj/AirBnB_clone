#!/usr/bin/python3
"""
Testcases for console.py cmd prompt
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
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


class TestShowCommand(unittest.TestCase):
    def test_show_without_id(self):
        """ test show command without id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            value = f.getvalue().strip("\n")
            output = "** instance id missing **"
            self.assertEqual(value, output)

    def test_show_base_model_plain(self):
        """ test show command on BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            bm = obj.get(f"BaseModel.{base_id}")
            self.assertIsNotNone(bm)
            b = BaseModel(**bm)
            self.assertEqual(str(b), value)
    
    def test_show_user_plain(self):
        """ test show command on User """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            u = obj.get(f"User.{base_id}")
            self.assertIsNotNone(u)
            b = User(**u)
            self.assertEqual(str(b), value)

    def test_show_state_plain(self):
        """ test show command on State """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            st = obj.get(f"State.{base_id}")
            self.assertIsNotNone(st)
            b = State(**st)
            self.assertEqual(str(b), value)

    def test_show_city__plain(self):
        """ test show command on City """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            ct = obj.get(f"City.{base_id}")
            self.assertIsNotNone(ct)
            b = City(**ct)
            self.assertEqual(str(b), value)

    def test_show_amenity_plain(self):
        """ test show command on Amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            am = obj.get(f"Amenity.{base_id}")
            self.assertIsNotNone(am)
            b = Amenity(**am)
            self.assertEqual(str(b), value)

    def test_show_place_plain(self):
        """ test show command on Place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            pl = obj.get(f"Place.{base_id}")
            self.assertIsNotNone(pl)
            b = Place(**pl)
            self.assertEqual(str(b), value)

    def test_show_review_plain(self):
        """ test show command on Review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            rv = obj.get(f"Review.{base_id}")
            self.assertIsNotNone(rv)
            b = Review(**rv)
            self.assertEqual(str(b), value)

    def test_show_base_model(self):
        """ test show command on BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            bm = obj.get(f"BaseModel.{base_id}")
            self.assertIsNotNone(bm)
            b = BaseModel(**bm)
            self.assertEqual(str(b), value)
    
    def test_show_user(self):
        """ test show command on User """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            u = obj.get(f"User.{base_id}")
            self.assertIsNotNone(u)
            b = User(**u)
            self.assertEqual(str(b), value)

    def test_show_state(self):
        """ test show command on State """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            st = obj.get(f"State.{base_id}")
            self.assertIsNotNone(st)
            b = State(**st)
            self.assertEqual(str(b), value)

    def test_show_city(self):
        """ test show command on City """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            ct = obj.get(f"City.{base_id}")
            self.assertIsNotNone(ct)
            b = City(**ct)
            self.assertEqual(str(b), value)

    def test_show_amenity(self):
        """ test show command on Amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            am = obj.get(f"Amenity.{base_id}")
            self.assertIsNotNone(am)
            b = Amenity(**am)
            self.assertEqual(str(b), value)

    def test_show_place(self):
        """ test show command on Place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            pl = obj.get(f"Place.{base_id}")
            self.assertIsNotNone(pl)
            b = Place(**pl)
            self.assertEqual(str(b), value)

    def test_show_review(self):
        """ test show command on Review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            rv = obj.get(f"Review.{base_id}")
            self.assertIsNotNone(rv)
            b = Review(**rv)
            self.assertEqual(str(b), value)


class TestDestroyCommand(unittest.TestCase):
    def test_destroy_without_id(self):
        """ test show command without id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            value = f.getvalue().strip("\n")
            output = "** instance id missing **"
            self.assertEqual(value, output)

    def test_destroy_base_model_plain(self):
        """ test destroy command on BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            bm = obj.get(f"BaseModel.{base_id}")
            self.assertIsNone(bm)
            self.assertEqual(value, '')
    
    def test_destroy_user_plain(self):
        """ test destroy command on User """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            u = obj.get(f"User.{base_id}")
            self.assertIsNone(u)
            self.assertEqual( value, '')

    def test_destroy_state_plain(self):
        """ test destroy command on State """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            st = obj.get(f"State.{base_id}")
            self.assertIsNone(st)
            self.assertEqual(value, '')

    def test_destroy_city__plain(self):
        """ test destroy command on City """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            ct = obj.get(f"City.{base_id}")
            self.assertIsNone(ct)
            self.assertEqual(value, '')

    def test_destroy_amenity_plain(self):
        """ test destroy command on Amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            am = obj.get(f"Amenity.{base_id}")
            self.assertIsNone(am)
            self.assertEqual(value, '')

    def test_destroy_place_plain(self):
        """ test destroy command on Place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            pl = obj.get(f"Place.{base_id}")
            self.assertIsNone(pl)
            self.assertEqual(value, '')

    def test_destroy_review_plain(self):
        """ test destroy command on Review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {base_id}")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            rv = obj.get(f"Review.{base_id}")
            self.assertIsNone(rv)
            self.assertEqual(value, '')

    def test_destroy_base_model(self):
        """ test destroy command on BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            bm = obj.get(f"BaseModel.{base_id}")
            self.assertIsNone(bm)
            self.assertEqual(value, '')
    
    def test_destroy_user(self):
        """ test destroy command on User """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            u = obj.get(f"User.{base_id}")
            self.assertIsNone(u)
            self.assertEqual(value, '')

    def test_destroy_state(self):
        """ test destroy command on State """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            st = obj.get(f"State.{base_id}")
            self.assertIsNone(st)
            self.assertEqual(value, '')

    def test_destroy_city(self):
        """ test destroy command on City """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            ct = obj.get(f"City.{base_id}")
            self.assertIsNone(ct)
            self.assertEqual(value, '')

    def test_destroy_amenity(self):
        """ test destroy command on Amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            am = obj.get(f"Amenity.{base_id}")
            self.assertIsNone(am)
            self.assertEqual(value, '')

    def test_destroy_place(self):
        """ test destroy command on Place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            pl = obj.get(f"Place.{base_id}")
            self.assertIsNone(pl)
            self.assertEqual(value, '')

    def test_destroy_review(self):
        """ test destroy command on Review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            base_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({base_id})")
            value = f.getvalue().strip("\n")
        with open("file.json") as fp:
            obj = json.load(fp)
            rv = obj.get(f"Review.{base_id}")
            self.assertIsNone(rv)
            self.assertEqual(value, '')
