import random

from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow


class Dojo:
    """All functionality is implemented here"""
    path = './files/'
    
    def __init__(self):
        self.occupants = []
        self.all_rooms = []
        self.all_staff = self.file_to_list_converter('./files/staff.txt')
        self.all_fellows = self.file_to_list_converter('./files/fellows.txt')
        self.all_livings = self.file_to_list_converter('./files/livings.txt')
        self.all_offices = self.file_to_list_converter('./files/offices.txt')
        self.all_pple_unallocated_office = self.file_to_list_converter(\
                                './files/all_pple_unallocated_office.txt')
        self.all_allocated_office = []
        self.fellows_want_living_unallocated = []
        self.fellows_living_allocated = []
        self.dict_livings = {}
        #self.dict_livings = self.write_read_dict_text(self.dict_livings, './files/dict_livings.txt', './files/dict_livings_r.txt')
        self.dict_offices = {}
        #self.dict_offices = self.write_read_dict_text(self.dict_offices, './files/dict_offices.txt', './files/dict_offices_r.txt')


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
        office_path = './files/offices.txt'
        living_path = './files/livings.txt'
        global dict_offices
        global dict_livings

  
        if room_type.lower() == "office":
            #self.all_offices = self.file_to_list_converter(office_path)
            for office in self.all_offices:
                if office == room_name:
                    print("Office already exists. Please try using a different name")
                    return
            # Write office name to offices.txt
            office_file = open(office_path, 'a')
            office_file.write(room_name + '\n')
            office_file.close() 
            # Add office to dict_offices dictionary
            self.dict_offices[room_name] = []
            self.all_offices = self.file_to_list_converter(office_path)
            print("Office " + room_name + " created successfully")
            print(self.dict_offices)
            print(self.all_offices)
        
        elif room_type.lower() == "living":
            for living in self.all_livings:
                if living == room_name:
                    print("Living space already exists. Please try using a different name")
                    return
            living_file = open(living_path, 'a')
            living_file.write(room_name + '\n')
            living_file.close() 
            # Add living space to dict_livings dictionary
            self.dict_livings[room_name] = []
            self.all_livings = self.file_to_list_converter(living_path)
            print("Living space " + room_name + " created successfully")
            print(self.dict_livings)
            print(self.all_livings)
            
            
    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person and allocate room"""

        global dict_offices
        global dict_livings
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
            self.all_fellows = self.file_to_list_converter(fellow_path)
            print(person_name + " has been added as a Fellow")

            # Allocate office to fellows
            available_office = self.get_random_room(self.dict_offices, 6)
            self.dict_offices[available_office].append(person_name)
            #self.dict_offices = self.write_read_dict_text(self.dict_offices, './files/dict_offices.txt', './files/dict_offices_r.txt')
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
            #self.dict_offices = self.write_read_dict_text(self.dict_offices, './files/dict_offices.txt', './files/dict_offices_r.txt')
            print(person_name + " has been allocated office " + available_office)
            print(self.dict_offices)

        else:
            print("Wrong person type entered. Please try again")

    def print_room(self, room_name):
        """Print people in the room"""
        global dict_offices
        global all_livings
        if room_name in self.all_offices:
            print(self.dict_offices[room_name])
        elif room_name in self.all_livings:
            print(self.dict_livings[room_name])
        else:
            print("The room does not exist. Please enter an existing one")


    def file_to_list_converter(self, afile):
        """Reads a file and returns a list based on the file contents"""
        alist = []
        try:
            file_ = open(afile, 'r')
            alist = file_.readlines()
            alist = [i.replace('\n','') for i in alist]
            file_.close()
        except:
            raise IOError("File not found")
        aset = set(alist)
        aset = list(aset)
        return aset 

    def allocate_room(self, person_name, person_type):
            """Allocates a room to a person"""
            # Get a random office that has space
            office_capacity = 6
            available_office = self.get_random_room(self.dict_offices, office_capacity)
            available_office.append(person_name)
            return available_office
            
    def write_read_dict_text(self, dict_to_read, write_file, read_file):
        """Writes a dictionary to a file and returns the updated dictionary"""
        dict_from_file = {}
        fout = write_file
        fout_r = read_file
        fo = open(fout, "w")
        fo_r = open(fout_r, "w")
        
        for k, v in dict_to_read.items():
            fo.write(str(k) + '\n' + ' ---------------------------------------- '+ '\n' + str(v) + '\n\n')
            fo_r.write(str(k) + ' = ' + str(v) + '\n')
        fo_r.close()
        fo.close()
        
        
        with open(read_file) as f:
            for line in f:
                k, v = line.strip().split(' = ')
                dict_from_file[k.strip()] = v.strip()
        
        f.close()
        return dict_from_file

                   