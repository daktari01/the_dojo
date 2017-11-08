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
        self.all_staff = []
        self.all_fellows = []
        self.all_offices = []
        self.all_livings = []
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
        office_path = './files/offices.txt'
        living_path = './files/livings.txt'

        if room_type.lower() == "office":
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
            self.all_offices = set(self.all_offices)
            # Read file and create a dictionary of offices
            
            if len(self.all_offices) > 0:
                self.dict_offices = dict.fromkeys(self.all_offices, [])
            else:
                print("The list is empty")
            print(self.dict_offices)
        
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
            # Get values of all fellows in fellows.txt file
            self.all_fellows = self.file_to_list_converter('./files/fellows.txt')
            print("Fellows at Andela are: \n")
            print(self.all_fellows)

            #create unallocated_office.txt 
            all_pple_unallocated_office_file = open(all_pple_unallocated_office_path, 'a')
            all_pple_unallocated_office_file.write(person_name + '\n')
            all_pple_unallocated_office_file.close()
            self.all_pple_unallocated_office.append(new_person)
            

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

            # Create all_pple_unallocated_office.txt 
            all_pple_unallocated_office_file = open(all_pple_unallocated_office_path, 'a')
            all_pple_unallocated_office_file.write(person_name + '\n')
            all_pple_unallocated_office_file.close()
            self.all_pple_unallocated_office.append(new_person)

            
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

        '''
        # Allocate person office
        office_capacity = 6
        available_office = self.get_random_room(self.dict_offices, office_capacity)
        self.all_livings = self.file_to_list_converter('./files/livings.txt')
        if len(self.all_livings) > 0:
            self.dict_livings = dict.fromkeys(self.all_livings, [])
        else:
            print("The list is empty")
        print(self.dict_livings)
        
        available_office.append(person_name)
        print(person_name + " + has been allocated office :" + available_office)
        '''
         

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

                   