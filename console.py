#!/usr/bin/python3
"""
This module serves as the entry point into the package
provides a command prompt to interact with
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __models = ("BaseModel", "User", "Amenity",
                "State", "City", "Place", "Review"
                )

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """This command Handles EOF\n"""
        print()
        return True

    def parseargs(self, line):
        """Parses the line args"""
        pattern = r'[\w-]+|(?:\"(?:\w+\W?\w*)+\")|(?:\'(?:\w+\W?\w*)+\')'
        commands = re.findall(pattern, line)
        stripped_commands = []
        for cmd in commands:
            stripped_commands.append(cmd.strip().strip("'").strip('"'))
        return stripped_commands

    def do_create(self, cls):
        """Creates a new instance of <cls> class\n\
Usage: create <class_name>\n"""
        if not cls:
            print("** class name missing **")
        else:
            cls = self.parseargs(cls)[0]
            if cls not in self.__models:
                print("** class doesn't exist **")
            else:
                b = eval(cls)()
                b.save()
                print(b.id)

    def do_show(self, line):
        """prints the string representation of an instance\
based on the class name and id\nUsage: show <class_name> <id>\n"""
        line = self.parseargs(line)
        ret = self.__class__.verify_rud_command(line)
        if ret:
            print(ret)

    def do_destroy(self, line):
        """prints the string representation of an instance\
based on the class name and id\nUsage: destroy <class_name> <id>\n"""
        line = self.parseargs(line)
        ret = self.__class__.verify_rud_command(line)
        if ret:
            storage.delete(ret)

    def do_all(self, option):
        """prints the string representation of all the instances \
based on/not based on the model name\nUsage: all <class_name>\
 (**<class_name> is optional**)\n"""
        filter_by = None
        if option:
            if option in self.__models:
                filter_by = option
            else:
                print("** class doesn't exist **")
                return None
        for key in storage.all().keys():
            if filter_by:
                if not key.startswith(filter_by):
                    continue
            class_name = storage.all()[key]["__class__"]
            obj = eval(class_name)(**storage.all()[key])
            print(obj)

    def do_update(self, line):
        """updates an instance basex on the class name and id\
by adding or updating attributes\nUsage: update <class_name> \
<id> <attribute name> "<attribute value>"\n"""
        line = self.parseargs(line)
        ret = self.__class__.verify_rud_command(line)
        if ret:
            cmd = line
            if len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("** value missing **")
            else:
                attr_name = cmd[2]
                attr_value = cmd[3]
                setattr(ret, attr_name, attr_value)
                storage.new(ret)
                storage.save()

    @classmethod
    def verify_rud_command(cls, cmd):
        """
        This is class method that verifies retrieve,
        update, and destroy (rud) commands and returns
        the id for printing
        """
        if len(cmd) < 1:
            print("** class name missing **")
        else:
            model_name = cmd[0]
            if model_name not in cls.__models:
                print("** class doesn't exist **")
            elif len(cmd) < 2:
                print("** instance id missing **")
            else:
                id = cmd[1]
                id = f"{model_name}.{id}"
                return (cls.find_id(id, model_name))
        return None

    @staticmethod
    def find_id(id, class_name):
        """
        A staticmethod that helps fetches the id for any
        retrieve, update, destroy operations
        """
        for key in storage.all().keys():
            if id == key:
                b = eval(class_name)(**storage.all()[key])
                return (b)
        print("** no instance found **")
        return None

    def update_dict(self, cl_name, id, obj_dict):
        """Update using a dictionary object"""
        for k, v in obj_dict.items():
            construct = f"{cl_name} {id} {k} {v}"
            self.do_update(construct)

    def emptyline(self):
        """Handles emptyline commands\n"""
        print(end="")

    def default(self, line):
        """Method to catch unknown commands"""
        pattern = re.findall(r"^(\w+)\.(\w+)(\((.*)\))$", line)
        if not len(pattern):
            return cmd.Cmd.default(self, line)
        class_name, operation, _, args = pattern[0]
        method_str = f"self.do_{operation}"
        if operation == "count":
            count = 0
            for key in storage.all().keys():
                if key.startswith(class_name):
                    count += 1
            print(count)
        else:
            option = class_name
            if args:
                p_split = r"^([\w\W]+),\s*(\{[\w\W]+\})\s*$"
                split_args = re.findall(p_split, args)
                if split_args and operation == "update":
                    id_arg = split_args[0][0]
                    dict_arg = split_args[0][1]
                    try:
                        dict_arg = eval(dict_arg)
                        if type(dict_arg) == dict:
                            self.update_dict(class_name, id_arg, dict_arg)
                    except Exception as e:
                        print(e)
                    return None
                option += " "
                option += " ".join([w.strip() for w in args.split(",")])
            option.strip()
            method = eval(method_str)
            method(option)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
