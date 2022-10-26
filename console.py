#!/usr/bin/python3
"""
This module serves as the entry point into the package
provides a command prompt to interact with
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __models = ("BaseModel",)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """This command Handles EOF\n"""
        print()
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel class\n\
Usage: create <class_name>\n"""
        if not cls:
            print("** class name missing **")
        else:
            if cls not in self.__models:
                print("** class doesn't exist **")
            else:
                b = BaseModel()
                b.save()
                print(b.id)
    
    def do_show(self, line):
        """prints the string representation of an instance\
based on the class name and id\nUsage: show <class_name> <id>\n"""
        ret = self.__class__.verify_rud_command(line)
        if ret:
            print(ret)

    def do_destroy(self, line):
        """prints the string representation of an instance\
based on the class name and id\nUsage: destroy <class_name> <id>\n"""
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
        ret = self.__class__.verify_rud_command(line)
        if ret:
            cmd = line.split(" ")
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
        split_line = cmd.split(" ")
        model_name = split_line[0].strip()
        if not model_name:
            print("** class name missing **")
        else:
            if model_name not in cls.__models:
                print("** class doesn't exist **")
            elif len(split_line) < 2:
                print("** instance id missing **")
            else:
                id = split_line[1].strip()
                id = f"{model_name}.{id}"
                return (cls.find_id(id))
        return None

    @staticmethod
    def find_id(id):
        """
        A staticmethod that helps fetches the id for any
        retrieve, update, destroy operations
        """
        for key in storage.all().keys():
            if id == key:
                b = BaseModel(**storage.all()[key])
                return (b)
        print("** no instance found **")
        return None

    def emptyline(self):
        """Handles emptyline commands\n"""
        print(end="")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
