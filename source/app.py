import cmd
import sys

from docopt import docopt, DocoptExit
from dojo import Dojo


"""
the_dojo

Usage: 
    create_room <room_type> <room_name> ...
    add_person <person_name> (FELLOW|STAFF) [wants_accommodation]
    
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
    def fn(self, args):
        try:
            option = docopt(fn.__doc__, args)
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
    prompt = '[dojo]>> '

    @the_dojo_docopt
    def do_create_room(self, args): 
        """
        Usage: create_room <room_type> <room_name> ...

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        for name in args['<room_name>']:
            Dojo().create_room(args['<room_type>'], name)
        print(args)
        

    @the_dojo_docopt
    def do_add_person(self, args): # remember to add <wants_accommodation>
        """
        Usage: add_person <person_name> <person_type> [<wants_accommodation>]

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        if args['<wants_accommodation>'] is None:
            Dojo().add_person(args['<person_name>'], args['<person_type>'])
        else: 
            Dojo().add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>'])
        # ['<person_name>'], ['<person_type>'], ['<wants_accommodation>']
        print(args)

    def do_quit(self, args):
        """Quits the_dojo"""
        exit()

if __name__ == '__main__':
    TheDojo().cmdloop()


