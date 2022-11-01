#!/usr/bin/python3
"""
Testcases for console.py cmd prompt
"""
from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO
import sys


class TestConsole(unittest.TestCase):

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

