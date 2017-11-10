import random

from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow


class Dojo:
    """All functionality is implemented here"""
    path = './files/'
    
    def __init__(self):
        self.occupants = []
        self.all_rooms = []
        self.all_staff = []
        self.all_fellows = []
        self.all_livings = []
        self.all_offices = []
        self.all_pple_unallocated_office = []
        self.all_allocated_office = []
        self.fellows_want_living_unallocated = []
        self.fellows_living_allocated = []
        self.dict_livings = {}
        self.dict_offices = {}
        

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
        global all_staff
        global all_fellows

  
        if room_type.lower() == "office":
            #self.all_offices = self.file_to_list_converter(office_path)
            for office in self.all_offices:
                if office == room_name:
                    print("Office already exists. Please try using a different name")
                    return
            # Add office to dict_offices dictionary
            self.dict_offices[room_name] = []
            self.all_offices.append(room_name)
            print("Office " + room_name + " created successfully")
            print(self.dict_offices)
            print(self.all_offices)
        
        elif room_type.lower() == "living":
            for living in self.all_livings:
                if living == room_name:
                    print("Living space already exists. Please try using a different name")
                    return
            # Add living space to dict_livings dictionary
            self.dict_livings[room_name] = []
            self.all_livings.append(room_name)
            print("Living space " + room_name + " created successfully")
            print(self.dict_livings)
            print(self.all_livings)
            
            
    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person and allocate room"""

        global dict_offices
        global dict_livings
        global all_livings
        global all_offices

        staff_path = './files/staff.txt'
        fellow_path = './files/fellows.txt'

        if person_type.upper() == 'FELLOW':
            for fellow in self.all_fellows:
                if fellow == person_name:
                    print("Fellow already exists!")
                    return
            new_person = Fellow(person_name)

            # Create fellows.txt to save names of fellows added
            fellow_file = open(fellow_path, 'a')
            fellow_file.write(person_name + '\n')
            fellow_file.close()
            self.all_fellows.append(person_name)
            print(person_name + " has been added as a Fellow")

            # Allocate office to fellows
            available_office = self.get_random_room(self.dict_offices, 6)
            self.dict_offices[available_office].append(person_name)
            print(person_name + " has been allocated office " + available_office)
            print(self.dict_offices)

        elif person_type.upper() == 'STAFF':
            for staff in self.all_staff:
                if staff == person_name:
                    print("Staff already exists!")
                    return
            new_person = Staff(person_name)

            # Create staff.txt to save names of staff added
            staff_file = open(staff_path, 'a')
            staff_file.write(person_name + '\n')
            staff_file.close()
            self.all_staff.append(new_person)

            # Allocate office to staff
            available_office = self.get_random_room(self.dict_offices, 6)
            self.dict_offices[available_office].append(person_name)
            print(person_name + " has been allocated office " + available_office)
            print(self.dict_offices)

        else:
            print("Wrong person type entered. Please try again")

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
            print("The room does not exist. Please enter an existing one")
        
        
    
    def print_allocations(self, print_rooms=None):
        """Print list of allocations"""
        global dict_offices
        global all_livings
        global all_offices
        global dict_livings
        
        if print_rooms is None:
            #print the rooms on the screen
            self.print_dict(dict_offices)
            self.print_dict(dict_livings)
        elif print_rooms == '-o':
            self.write_to_dict(self.dict_offices, './files/allocations.txt')
            self.write_to_dict(self.dict_livings, './files/allocations.txt')
            
    def print_dict(self, dict_):
        """Prints the dictionary"""
        for key, value in dict_.items():
            print(str(key).upper() + '\n'+'-------------------------------'+'\n' + str(', '.join(value)) + '\n\n')
            
    def write_to_dict(self, dict_to_read, write_file):
        """Writes dictionary to file"""
        fout = write_file
        fo = open(fout, "a")
        
        for key, value in dict_to_read.items():
            fo.write(str(key).upper() + '\n'+'-------------------------------'+'\n' + str(', '.join(value)) + '\n\n')
        fo.close()
        

        

                            