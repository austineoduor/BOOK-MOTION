#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.bookmotion_base import BookMotionBase
from models.user import User
from models.book import Book
from models.book_recommended import Recommended
from shlex import split

class BookMotionCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    intro = 'Welcome to the BookMotion shell.   Type help or ? to list commands.\n'
    prompt = "(BookMotion) "
    classes = {"BookMotionBase","User","Book","Recommended"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            obj = eval("{}()".format(my_list[0]))
            print("{}".format(obj.id))
            for num in range(1, len(my_list)):
                my_list[num] = my_list[num].replace('=', ' ')
                attributes = split(my_list[num])
                attributes[1] = attributes[1].replace('_', ' ')
                try:
                    var = eval(attributes[1])
                    attributes[1] = var
                except:
                    pass
                if type(attributes[1]) is not tuple:
                    setattr(obj, attributes[0], attributes[1])
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Print string representation: name and id
        Example: show BookMotionBase d23d2e1e-4ac2-45d2-b854-9cf9d07d9e4d
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in BookMotionCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file
        Example: destroy BookMotionBase d23d2e1e-4ac2-45d2-b854-9cf9d07d9e4d
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in BookMotionCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class
        Example: all BookMotionBase or all
        """
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs.__str__())
            print(obj_list)
        elif args[0] in BookMotionCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs.__str__())
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attribute
        Example: update LibrarifyBase 1234-1234-1234 email "librarify@mail.com"
        """
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in BookMotionCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display count of instances specified
        Example: count LibrarifyBase
        """
        if line in BookMotionCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())

if __name__ == "__main__":
    BookMotionCommand().cmdloop()
