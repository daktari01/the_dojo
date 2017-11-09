import random

from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow


class Dojo:
    """All functionality is implemented here"""
    path = './files/'
    def __init__(self):
        self.occupants = []
        self.all_rooms = []
        self.all_people = []
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
        self.dict_livings = self.write_read_dict_text(self.dict_livings, './files/dict_livings.txt', './files/dict_livings_r.txt')
        self.dict_offices = {}
        self.dict_offices = self.write_read_dict_text(self.dict_offices, './files/dict_offices.txt', './files/dict_offices_r.txt')
        
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

        
        if room_type.lower() == "office":
            #self.all_offices = self.file_to_list_converter(office_path)
            for office in self.all_offices:
                if office == room_name:
                    print("Office already exists. Please try using a different name")
                    return
            office_file = open(office_path, 'a')
            office_file.write(room_name + '\n')
            office_file.close() 
            new_office = Office(room_name)
             #Remember to sort the duplicate living thingie
            # Get a list of all offices
            self.all_offices = self.file_to_list_converter(office_path)
            # Read file and create a dictionary of offices
            
            if len(self.all_offices) > 0:
                self.dict_offices = dict.fromkeys(self.all_offices, [])
            else:
                print("The list is empty")
            
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
            new_living = LivingSpace(room_name)
            #Remember to sort the duplicate living thingie
            # Get a list of all living spaces
            self.all_livings = self.file_to_list_converter(living_path)
            #self.all_livings = set(self.all_livings)
            # Read file and create a dictionary of living spaces
            if len(self.all_livings) > 0:
                self.dict_livings = dict.fromkeys(self.all_livings, [])
            else:
                print("The list is empty")
            print(self.dict_livings)

            
    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person and allocate room"""

        staff_path = './files/staff.txt'
        fellow_path = './files/fellows.txt'
        all_people_path = './files/all_people.txt'
        all_pple_unallocated_office_path = './files/all_pple_unallocated_office.txt'
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
            self.all_fellows.append(new_person)
            self.all_people.append(new_person)
            
            # Create unallocated_office.txt 
            all_pple_unallocated_office_file = open(all_pple_unallocated_office_path, 'a')
            all_pple_unallocated_office_file.write(person_name + '\n')
            all_pple_unallocated_office_file.close()

            # Generate dictionary from list of offices
            if len(self.all_offices) > 0:
                #self.dict_offices = dict.fromkeys(self.all_offices, [])
                keys = self.all_offices
                value = []
                self.dict_offices = {key: list(value) for key in keys}
            else:
                print("The list is empty")
            # Allocate office to fellows
            available_office = self.get_random_room(self.dict_offices, 6)
            self.dict_offices[available_office].append(person_name)
            self.dict_offices = self.write_read_dict_text(self.dict_offices, './files/dict_offices.txt', './files/dict_offices_r.txt')
            print(person_name + " has been allocated office " + available_office)
            print(self.dict_offices)
            # Write the self.dict_offices to a file and instantiate self.dict_offices 
            # to read from that file
            '''
            # Allocate living rooms to fellows
            if wants_accommodation == 'Y' or wants_accommodation == 'y':
                if len(self.all_livings) > 0:
                    self.dict_livings = dict.fromkeys(self.all_livings, [])
                else:
                    print("The list is empty")
            '''


            '''
            # Remove person from unallocated list
            file_allocated = open('./files/all_pple_unallocated_office.txt', 'r')
            allocated_lines = file_allocated.readlines
            file_allocated.close()
            file_allocated = open('./files/all_pple_unallocated_office.txt', 'w')
            for line in allocated_lines:
                if line != person_name + "\n":
                    file_allocated.write(line)
            file_allocated.close()
            '''
            # ##remember to compare len(dict[person_name]) to be less than 6 before allocating. 
            # If it is >= 6, pick another random room 
            # ##add the person to allocated list

            

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
            self.all_people.append(new_person)
            # Get values of all staff in staff.txt file
            self.all_staff = self.file_to_list_converter('./files/staff.txt')
            #print("Staff at Andela are: \n")
            print(self.all_staff)

            
        else:
            print("Wrong person type entered. Please try again")

        # Add people from fellow.txt file and staff.txt to get all_people.txt
        filenames = [fellow_path, staff_path]
        with open(all_people_path, 'w') as all_people_file:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        all_people_file.write(line)
        all_people_file.close()

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

                   