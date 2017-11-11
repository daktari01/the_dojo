import random


from termcolor import colored
from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow


class Dojo:
    """All functionality is implemented here"""
    path = './files/'
    
    def __init__(self):
        self.all_staff = []
        self.all_fellows = []
        self.all_livings = []
        self.all_offices = []
        self.unallocated_people = []
        self.dict_livings = {}
        self.dict_offices = {}
        self.dict_all_rooms = {}

    def check_available_space(self, room_dict, room_capacity):
        """Checks whether there is space in rooms"""
        return any(room_capacity > len(values) for values in room_dict.values())   

    def get_random_room(self, room_dict, room_capacity):
        """Returns a random room that has available space"""
        # Pick a random key from the dictionary
        random_key = random.choice(list(room_dict))
        while room_capacity == len(room_dict[random_key]):
            random_key = random.choice(list(room_dict))
        return random_key

    def create_room(self, room_type, room_name):
        """Method to create rooms and allocate"""
        new_offices = []
        new_livings =[]

        global dict_offices 
        global dict_livings
        global all_offices
        global all_livings

        if room_type.lower() == "office":
            for office in self.all_offices:
                if office == room_name:
                    print(colored("Office already exists."\
                            +" Please try using a different name", 'red'))
                    return
            # Add office to dict_offices dictionary
            self.dict_offices[room_name] = []
            self.all_offices.append(room_name)
            print(colored("Office " + room_name \
                                    + " created successfully", 'green'))

        elif room_type.lower() == "living":
            for living in self.all_livings:
                if living == room_name:
                    print(colored("Living space already exists."\
                            +" Please try using a different name", 'red'))
                    return
            # Add living space to dict_livings dictionary
            self.dict_livings[room_name] = []
            self.all_livings.append(room_name)
            print(colored("Living space " + room_name \
                                        + " created successfully", 'green'))
              
    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person and allocate room"""

        global dict_offices
        global dict_livings
        global all_livings
        global all_offices
        global unallocated_people

        if person_type.upper() == 'FELLOW':
            for fellow in self.all_fellows:
                if fellow == person_name:
                    print(colored("Fellow already exists!", 'red'))
                    return
            
            
            # Check if any office has space
            if self.check_available_space(self.dict_offices, 6) is True:
                self.all_fellows.append(person_name)
                print(colored(person_name \
                        + " has been added as a Fellow", 'yellow'))
                # Allocate office to fellows
                available_office = self.get_random_room(self.dict_offices, 6)
                self.dict_offices[available_office].append(person_name)
                print(colored(person_name + " has been allocated office " \
                                            + available_office, 'yellow'))
            else:
                # When no office has space
                self.all_fellows.append(person_name)
                print(colored(person_name \
                                + " has been added as a Fellow", 'yellow'))
                print(colored("There is no available office to add " + person_name \
                                        + ". Create one first", 'red'))
                self.unallocated_people.append(person_name)

            # Check if any living space has space
            if wants_accommodation == 'Y' or wants_accommodation == 'y':
                if self.check_available_space(self.dict_livings, 4) is True:
                    available_living = self.get_random_room(self.dict_livings, 4)
                    #if wants_accommodation == 'Y' or wants_accommodation == 'y':
                    # Allocate living space to fellows
                    self.dict_livings[available_living].append(person_name)
                    print(colored(person_name + " has been allocated living space " \
                                            + available_living, 'yellow'))
                else:
                    # When no living space has space
                    self.all_fellows.append(person_name)
                    print(colored(person_name \
                                + " has been added as a Fellow", 'yellow'))
                    print(colored("There is no available living space to add " \
                                + person_name + ". Create one first", 'red'))
                    self.unallocated_people.append(person_name)

        elif person_type.upper() == 'STAFF':
            for staff in self.all_staff:
                if staff == person_name:
                    print(colored("Staff already exists!", 'red'))
                    return
            new_person = Staff(person_name)

            # Add new staff to all_staff list
            self.all_staff.append(new_person)
            print(colored(person_name + " has been added as a Staff", 'yellow'))

            # Allocate office to staff
            available_office = self.get_random_room(self.dict_offices, 6)
            self.dict_offices[available_office].append(person_name)
            print(colored(person_name + " has been allocated office " \
                                            + available_office, 'yellow'))

        else:
            print(colored("Wrong person type entered. Please try again", 'red'))

    def print_room(self, room_name):
        """Print people in the room"""
        global dict_offices
        global all_livings
        global all_offices
        global dict_livings
        
        if room_name in self.all_offices:
            print(', '.join(self.dict_offices[room_name]))
        elif room_name in self.all_livings:
            print(', '.join(self.dict_livings[room_name]))
        else:
            print(colored("The room does not exist. Please enter an existing one", 'red'))
        
    
    def print_allocations(self, print_rooms=None):
        """Print list of allocations"""
        global dict_offices
        global all_livings
        global all_offices
        global dict_livings
        global unallocated_people
        
        #Add the office dictionary and the livings one
        dict_all_rooms = dict(self.dict_offices, **self.dict_livings)
        
        if print_rooms is None:
            for key, value in dict_all_rooms.items():
                print(str(key).upper() + '\n'+'-------------------------------'\
                                        +'\n' + str(', '.join(value)) + '\n\n')
                
        elif print_rooms == '-o':
            self.write_dict_to_file(dict_all_rooms, './files/allocations.txt')
            print(colored("The result has been written" \
                                    + "to file allocations.txt", 'yellow'))
    
    def print_unallocated(self, print_pple=None):
        """Prints list of unallocated people"""
        if print_pple is None:
            for unallocated in self.unallocated_people:
                print(unallocated + "\n")
        
        else: 
            # Write to file
            unallocated_file = open('./files/unallocated.txt', 'w')
            for unallocated in self.unallocated_people:
                unallocated_file.write(unallocated + "\n")
            unallocated_file.close()
            print(colored("The result has been" \
                        + "written to file unallocated.txt", 'yellow'))

    
    def write_dict_to_file(self, dict_to_read, write_file):
        """Writes dictionary to file"""
        fout = write_file
        fo = open(fout, "w")
        for key, value in dict_to_read.items():
            fo.write(str(key).upper() + '\n'+'-------------------------------'\
                                        +'\n' + str(', '.join(value)) + '\n\n')
        fo.close()
                        