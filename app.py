import cmd
import sys

from docopt import docopt, DocoptExit
from source.dojo import Dojo


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
    This decorator is used to pass the result of the docopt parsing to \
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
    # Print the_dojo graphic
    '''
    print("****** " + " **  ** " + " ****** " + "   " + "***    " + "  ****  " \
                    + "     ** " + "  ****  ")
    print("****** " + " **  ** " + " ****** " + "   " + "*****  " + " ****** " \
                    + "     ** " + " ****** ")
    print("  **   " + " **  ** " + " **     " + "   " + "**  ** " + " **  ** " \
                    + "     ** " + " **  ** ")
    print("  **   " + " ****** " + " *****  " + "   " + "**  ** " + " **  ** " \
                    + "     ** " + " **  ** ")
    print("  **   " + " ****** " + " *****  " + "   " + "**  ** " + " **  ** " \
                    + " **  ** " + " **  ** ")
    print("  **   " + " **  ** " + " **     " + "   " + "**  ** " + " **  ** " \
                    + " **  ** " + " **  ** ")
    print("  **   " + " **  ** " + " ****** " + "   " + "*****  " + " ****** " \
                    + " ****** " + " ****** ")
    print("  **   " + " **  ** " + " ****** " + "   " + "***    " + "  ****  " \
                    + "  ****  " + "  ****  ")
    '''

    intro = "Welcome to the_dojo program!"  \
        + " Type help for a list of commands"

    prompt = '[dojo]>> '


    @the_dojo_docopt
    def do_add_person(self, args):
        """
        Usage: add_person <person_name> <person_type> [<wants_accommodation>]

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        if args['<person_type>'].lower() == 'staff' and args['<wants_accommodation>'] is not None:
            print("Staff cannot be allocated living spaces")
        elif args['<person_type>'].lower() == 'staff' and args['<wants_accommodation>'] is None:
            Dojo().add_person(args['<person_name>'], args['<person_type>'])
            print(args['<person_name>'] + " has been added as a Staff")
        elif args['<person_type>'].lower() == 'fellow' and args['<wants_accommodation>'] is None:
            Dojo().add_person(args['<person_name>'], args['<person_type>'])
            print(args['<person_name>'] + " has been added as a Fellow")
        elif args['<person_type>'].lower() == 'fellow' and args['<wants_accommodation>'] == 'Y':
            Dojo().add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>'])
            print(args['<person_name>'] + " has been added as a Fellow")
        elif args['<person_type>'].lower() == 'fellow' and args['<wants_accommodation>'] == 'y':
            Dojo().add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>'])
            print(args['<person_name>'] + " has been added as a Fellow")
        elif args['<person_type>'].lower() == 'fellow' and args['<wants_accommodation>'] == 'N':
            Dojo().add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>'])
            print(args['<person_name>'] + " has been added as a Fellow")
        elif args['<person_type>'].lower() == 'fellow' and args['<wants_accommodation>'] == 'n':
            Dojo().add_person(args['<person_name>'], args['<person_type>'], args['<wants_accommodation>'])
            print(args['<person_name>'] + " has been added as a Fellow")
        else:
            print("Wrong inputs entered. Type 'help add_person' for help")


    @the_dojo_docopt
    def do_create_room(self, args): 
        """
        Usage: create_room <room_type> <room_name> ...

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        if args['<room_type>'].lower() == 'office' or args['<room_type>'].lower() == 'living':
            for name in args['<room_name>']:
                Dojo().create_room(args['<room_type>'], name)
                print(args['<room_type>'] + " " + name + " created successfully")
        else:
            print("Wrong room type entered")

    def do_quit(self, args):
        """Quits the_dojo"""
        print("Thank you for using the_dojo. Goodbye!")
        exit()

if __name__ == '__main__':
    TheDojo().cmdloop()


