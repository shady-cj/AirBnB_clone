#!/usr/bin/python3
"""
This module serves as the entry point into the package
provides a command prompt to interact with
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """This command Handles EOF\n"""
        print()
        return True

    def emptyline(self):
        """Handles emptyline commands\n"""
        print(end="")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
