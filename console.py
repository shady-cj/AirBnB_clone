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

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """This command Handles EOF\n"""
        print()
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel class\n"""
        if not cls:
            print("** class name missing **")
        else:
            if cls != "BaseModel":
                print("** class doesn't exist **")
            else:
                b = BaseModel()
                b.save()
                print(b.id)
    
    def do_show(self, line):
        """prints the string representation of an instance\
based on the class name and id\n"""

        split_line = line.split(" ")
        cls = split_line[0].strip()
        if not cls:
            print("** class name missing **")
        else:
            if cls != "BaseModel":
                print("** class doesn't exist **")
            elif len(split_line) < 2:
                print("** instance id missing **")
            else:
                id = split_line[1].strip()
                present = False
                print(storage.all())
                for key in storage.all().keys():
                    if f"BaseModel.{id}" == key:
                        present = True
                        b = BaseModel(**storage.all()[key])
                        print(b)
                if not present:
                    print("** no instance found **")
    def emptyline(self):
        """Handles emptyline commands\n"""
        print(end="")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
