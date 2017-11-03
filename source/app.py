import cmd
import sys

from docopt import docopt, DocoptExit
from dojo import Dojo


"""
the_dojo

Usage: 
    create_room <room_type> <room_name> ...
    add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    
Options:
    room_type               Type of room, either office or living space.
    room_name               Name of room to create.
    person_name             Name of the person to be created
    wants_accommodation     Whether person wants accommodation or not. [default: N]
    -h --help               Show this screen.
    --version               Show version.
    -q                      Quit.
    
"""
def the_dojo_docopt(func):
    """
    This decorator is used to pass the result of the docopt parsing to 
    the called action
    """
    def fn(self, argument):
        try:
            option = docopt(fn.__doc__, argument)
        except DocoptExit as e:
            #The DocoptExit is thrown when the arguments do not match
            #A message to the user is printed and the usage
            print("Invalid command!")
            print(e)
            return
        return func(self, option)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class TheDojo(cmd.Cmd):
    intro = "Welcome to the_dojo program!"  \
        + "(type help for a list of commands)"
    prompt = '[dojo]> '

    @the_dojo_docopt
    def do_create_room(self, argument): #add elipse!!
        """
        Usage: create_room <room_type> <room_name> ...

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. 
                                        [default: N]
        """
        for name in argument['<room_name>']:
            print (Dojo().create_room(argument['<room_type>'], name))
        # print(argument)
        

    @the_dojo_docopt
    def do_add_person(self, argument):
        """
        Usage: add_person <person_name> <FELLOW|STAFF> [wants_accommodation]

        Options:
            room_type       Type of room, either office or living space.
            room_name       Name of room to create.
        """
        print(argument)

    def do_quit(self, argument):
        """Quits the_dojo"""
        exit()

if __name__ == '__main__':
    TheDojo().cmdloop()


