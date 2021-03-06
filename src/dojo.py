import random


from termcolor import colored
from src.room import Room, Office, LivingSpace
from src.person import Person, Staff, Fellow


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
                self.unallocated_people.append(person_name + " - lacks office space")

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
                    print(colored("There is no available living space to add " \
                                + person_name + ". Create one first", 'red'))
                    self.unallocated_people.append(person_name + " - lacks living space")

        elif person_type.upper() == 'STAFF':
            for staff in self.all_staff:
                if staff == person_name:
                    print(colored("Staff already exists!", 'red'))
                    return
            # Check if any office has space    
            if self.check_available_space(self.dict_offices, 6) is True:
                available_office = self.get_random_room(self.dict_offices, 6)
                # Add new staff to all_staff list
                self.all_staff.append(person_name)
                print(colored(person_name + " has been added as a Staff", 'yellow'))

                # Allocate office to staff
                
                self.dict_offices[available_office].append(person_name)
                print(colored(person_name + " has been allocated office " \
                                                + available_office, 'yellow'))
            else:
                self.all_staff.append(person_name)
                print(colored(person_name + " has been added as a Staff", 'yellow'))
                print(colored("There is no available office to add " \
                            + person_name + ". Create one first", 'red'))
                self.unallocated_people.append(person_name + " - lacks office space")

        else:
            print(colored("Wrong person type entered. Please try again", 'red'))

    def print_room(self, room_name):
        """Print people in the room"""
        global dict_offices
        global all_livings
        global all_offices
        global dict_livings
        
        if room_name in self.all_offices:
            if len(self.dict_offices[room_name]) != 0:
                print(', '.join(self.dict_offices[room_name]))
            else:
                print(colored("Office " + room_name + " is empty.", 'yellow'))
        elif room_name in self.all_livings:
            if len(self.dict_livings[room_name]) != 0:
                print(', '.join(self.dict_livings[room_name]))
            else:
                print(colored("Living space " + room_name + " is empty.", 'yellow'))
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
        if len(self.unallocated_people) > 0:
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
        else:
            print(colored("There are no unallocated people.", 'yellow'))

    def reallocate_person(self, person_name, new_room):
        """Moves a person from one room to another"""
        global dict_offices 
        global dict_livings
        global all_offices
        global all_livings
        
        if new_room in self.all_offices or new_room in self.all_livings:
            if self.check_which_room_person_is(person_name, self.dict_offices) or \
                self.check_which_room_person_is(person_name, self.dict_livings)\
                         is not False:
                if self.check_which_room_person_is(person_name, self.dict_offices) \
                    or self.check_which_room_person_is(person_name, self.dict_livings) \
                    != new_room:
                    if new_room in self.all_offices:
                        if self.room_has_space(self.dict_offices[new_room], 6) is True:
                            try:
                                current_room = self.check_which_room_person_is(person_name, self.dict_offices)
                                self.dict_offices[current_room].remove(person_name)
                                self.dict_offices[new_room].append(person_name)
                                print(colored(person_name + " successfully reallocated to " + new_room, 'green'))
                            except:
                                print(colored(current_room + " must be an office for reallocation to occur.", 'red'))
                        else:
                            print(colored(new_room + " is full. Please try again"))
                    elif new_room in self.all_livings:
                        if self.room_has_space(self.dict_livings[new_room], 4) is True:
                            try:
                                current_room = self.check_which_room_person_is(person_name, self.dict_livings)
                                self.dict_livings[current_room].remove(person_name)
                                self.dict_livings[new_room].append(person_name)
                                print(colored(person_name + " successfully reallocated to " + new_room, 'green'))
                            except:
                                print(colored(current_room + " must be a living space for reallocation to occur.", 'red'))
                        else:
                            print(colored(new_room + " is full. Please try again"))
                    else:
                        print(colored(new_room + " does not exist in the system. Create it first.", 'red'))
                else:
                    print(colored("A person cannot be reallocated to the same room. "\
                                            +"Please select a different room", 'red'))
            else:
                print(colored(person_name + " does not exist in any of the "\
                    +"rooms. Reallocation is only done for persons with a "\
                    +"room already", 'red'))
        else:
            print(colored(new_room + " does not exist. "\
                +"You can only reallocate a person to an existing room", 'red'))

    def allocate_room(self, person_name, room_type):
        """Allocates rooms to unallocated people"""
        global dict_offices 
        global dict_livings
        global all_offices
        global all_livings
    
        if (person_name + " - lacks " + room_type.lower() + " space") in self.unallocated_people:
            for unallocated in self.unallocated_people:
                unallocated_item = unallocated.split()
                full_name = '{} {}'.format(unallocated_item[0], unallocated_item[1])
                #if person_name == full_name and room_type.lower() == unallocated_item[4]:
                if room_type == 'office':
                    try:
                        available_office = self.get_random_room(self.dict_offices, 6)
                        self.dict_offices[available_office].append(person_name)
                        print(colored(person_name + " has been allocated office " \
                                                    + available_office, 'yellow'))
                        self.unallocated_people.remove(unallocated)
                    except:
                        print(colored("There is no available office to allocate " + person_name, 'red'))
                else: 
                    try:
                        available_living = self.get_random_room(self.dict_livings, 4)
                        self.dict_livings[available_living].append(person_name)
                        print(colored(person_name + " has been allocated living space " \
                                                + available_living, 'yellow'))
                        self.unallocated_people.remove(unallocated)
                    except:
                        print(colored("There is no available living space to allocate " + person_name, 'red'))
                break
        else:
            print(colored(person_name + " does not exist among the unallocated people", 'red'))

    def load_people(self):
        """Loads people from a text file"""
        with open('./files/load_people.txt', 'r') as load_file:
            for line in load_file:
                line = line.split()
                full_name = '{} {}'.format(line[0], line[1])
                if len(line) == 4:
                    self.add_person(full_name, line[2], line[3])
                elif len(line) == 3:
                    self.add_person(full_name, line[2])

    def write_dict_to_file(self, dict_to_read, write_file):
        """Writes dictionary to file"""
        fout = write_file
        fo = open(fout, "w")
        for key, value in dict_to_read.items():
            fo.write(str(key).upper() + '\n'+'-------------------------------'\
                                        +'\n' + str(', '.join(value)) + '\n\n')
        fo.close()


    def check_which_room_person_is(self, person_name, room_dict):
        for room_name, name_list in room_dict.items():
            if person_name in name_list:
                return room_name
        return False
                        
    def room_has_space(self, room_name, capacity):
        """Checks whether a single room has space"""
        if len(room_name) < capacity:
            return True
        return False

    def room_is_empty(self, room_name):
        """Tests whether the room is empty"""
        if room_name in self.all_offices:
            if len(self.dict_offices[room_name]) == 0:
                return True
            else:
                return False
        elif room_name in self.all_livings:
            if len(self.dict_livings[room_name]) == 0:
                return True
            else:
                return False
        else:
            return False

    

    

    