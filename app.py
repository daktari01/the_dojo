"""
Usage: 
    create_room <room_type> <room_name> ...
    add_person <person_name> (FELLOW|STAFF) [wants_accommodation]
    print_room <room_name>
    print_allocations [-o=filename]
    print_unallocated [-o=filename]
    reallocate_person <person_identifier> <new_room_name>
    allocate_room <room_type> <first_name> <second_name>
    load_people
    
Options:
    room_type               Type of room, either office or living space.
    room_name               Name of room to create.
    person_name             Name of the person to be created
    wants_accommodation     Whether person wants accommodation or not. [default: N]
    -h --help               Show the usage.
    --version               Show version.
    quit                      Quit.
    
"""

import cmd
import sys

from termcolor import colored
from docopt import docopt, DocoptExit
from src.dojo import Dojo

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
            print(colored("Invalid command!", 'red'))
            print(colored(e, 'yellow'))
            return
        return func(self, option)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class TheDojo(cmd.Cmd):
    # Print the_dojo graphic
    
    print(colored("****** " + " **  ** " + " ****** " + "   " + "***    " + "  ****  " \
                    + "     ** " + "  ****  ", 'blue'))
    print(colored("****** " + " **  ** " + " ****** " + "   " + "*****  " + " ****** " \
                    + "     ** " + " ****** ", 'blue'))
    print("  **   " + " **  ** " + " **     " + "   " + "**  ** " + " **  ** " \
                    + "     ** " + " **  ** ")
    print(colored("  **   " + " ****** " + " *****  " + "   " + "**  ** " + " **  ** " \
                    + "     ** " + " **  ** ", 'red'))
    print(colored("  **   " + " ****** " + " *****  " + "   " + "**  ** " + " **  ** " \
                    + " **  ** " + " **  ** ", 'red'))
    print("  **   " + " **  ** " + " **     " + "   " + "**  ** " + " **  ** " \
                    + " **  ** " + " **  ** ")
    print(colored("  **   " + " **  ** " + " ****** " + "   " + "*****  " + " ****** " \
                    + " ****** " + " ****** ", 'green'))
    print(colored("  **   " + " **  ** " + " ****** " + "   " + "***    " + "  ****  " \
                    + "  ****  " + "  ****  ", 'green'))
    

    prompt = '[dojo]>> '

    dojo = Dojo()
    
    @the_dojo_docopt
    def do_add_person(self, args):
        """
        Usage: add_person <first_name> <second_name> <person_type> [<wants_accommodation>]

        Options:
            first_name              First name of the person to be added
            second_name             Second name of the person to be added
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        if args['<first_name>'].isalpha() and args['<second_name>'].isalpha():
            person_name = '{} {}'.format(args['<first_name>'], \
                                        args['<second_name>'])
            if args['<person_type>'].lower() == 'staff' \
                                    and args['<wants_accommodation>'] is not None:
                print(colored("Staff cannot be allocated living spaces", 'red'))
            elif args['<person_type>'].lower() == 'staff' \
                                        and args['<wants_accommodation>'] is None:
                self.dojo.add_person(person_name, args['<person_type>'])
            elif args['<person_type>'].lower() == 'fellow' \
                                        and args['<wants_accommodation>'] is None:
                self.dojo.add_person(person_name, args['<person_type>'])
            elif args['<person_type>'].lower() == 'fellow' \
                                        and args['<wants_accommodation>'] == 'Y':
                self.dojo.add_person(person_name, args['<person_type>'], \
                                                    args['<wants_accommodation>'])
            elif args['<person_type>'].lower() == 'fellow' \
                                        and args['<wants_accommodation>'] == 'y':
                self.dojo.add_person(person_name, args['<person_type>'], \
                                                    args['<wants_accommodation>'])
            elif args['<person_type>'].lower() == 'fellow' \
                                        and args['<wants_accommodation>'] == 'N':
                self.dojo.add_person(person_name, args['<person_type>'], \
                                                    args['<wants_accommodation>'])
            elif args['<person_type>'].lower() == 'fellow' \
                                        and args['<wants_accommodation>'] == 'n':
                self.dojo.add_person(person_name, args['<person_type>'], \
                                                    args['<wants_accommodation>'])
            else:
                print(colored("Wrong inputs entered." \
                                    + "Type 'help add_person' for help", 'red'))
        else:
            print(colored("Person name can only contain aplhabets. Please try again", 'red'))


    @the_dojo_docopt
    def do_create_room(self, args): 
        """
        Usage: create_room <room_type> <room_name> ...

        Options:
            person_name             Name of the person to be created
            wants_accommodation     Whether person wants accommodation or not. [default: N]
        """
        if args['<room_type>'].lower() == 'office' or args['<room_type>']\
                                                        .lower() == 'living':
            for name in args['<room_name>']:
                if name.isalpha():
                    self.dojo.create_room(args['<room_type>'], name)
                else:
                    print(colored("Room "+name+" not created. Ensure that "\
                            +"it only contains alphabets", 'red'))
        else:
            print(colored("Wrong room type entered", 'red'))

    @the_dojo_docopt
    def do_print_room(self, args):
        """
        Usage: print_room <room_name>

        Options:
        room_name             Name of the room whose occupants to list
        """
        self.dojo.print_room(args['<room_name>'])

    @the_dojo_docopt
    def do_print_allocations(self, arg_o):
        """
        Usage: print_allocations [-o]
        
        Options:
        -o              Save to a file or not [default:filename]
        """
        if arg_o["-o"]:
            self.dojo.print_allocations('-o')
        else:
            self.dojo.print_allocations()

    @the_dojo_docopt
    def do_print_unallocated(self, arg_o):
        """
        Usage: print_unallocated [-o]
        
        Options:
        -o              Save to a file or not [default:filename]
        """
        if arg_o["-o"]:
            self.dojo.print_unallocated('-o')
        else:
            self.dojo.print_unallocated()

    @the_dojo_docopt
    def do_reallocate_person(self, args):
        """
        Usage: reallocate_person <first_name> <second_name> <new_room_name>

        Options:
        new_room_name               Name of the room to transfer person to.
        """
        person_name = '{} {}'.format(args['<first_name>'], \
                                        args['<second_name>'])
        self.dojo.reallocate_person(person_name, args['<new_room_name>'])

    @the_dojo_docopt
    def do_allocate_room(self, args):
        """
        Usage: allocate_room <room_type> <first_name> <second_name>
        """
        person_name = '{} {}'.format(args['<first_name>'], \
                                        args['<second_name>'])
        self.dojo.allocate_room(person_name, args['<room_type>'])
        
    @the_dojo_docopt
    def do_load_people(self, args):
        """
        Usage: load_people
        """
        self.dojo.load_people()
    
    def do_quit(self, args):
        """Quits the_dojo"""
        print(colored("Thank you for using the_dojo. Goodbye!", 'yellow'))
        exit()

if __name__ == '__main__':
    print(colored(__doc__, 'cyan'))
    TheDojo().cmdloop()
