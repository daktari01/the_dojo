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
        self.dict_livings = {}
        self.dict_offices = {}
    
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
            # Get a list of all offices 
            if len(self.all_offices) > 0:
                for office in self.all_offices:
                    self.dict_offices = {[office]:[]}
            else:
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
            '''
            if len(self.all_livings) > 0:
                for living in self.all_livings:
                    self.dict_livings = {[living]:[]}
            else:
                print("The list is empty")
            '''
            for living in self.all_livings:
                self.dict_livings = {[living]:[]}
                print(self.dict_livings)



    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person and allocate room"""
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
            self.all_fellows.append(new_person)
            self.all_people.append(new_person)
            # Get values of all fellows in fellows.txt file
            self.all_fellows = self.file_to_list_converter('./files/fellows.txt')

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
            # Join the all_fellows and all_staff lists to obtain all_people list
            self.all_people = self.all_fellows.extend(self.all_staff)

        else:
            print("Wrong person type entered. Please try again")
        return self.all_people

    def file_to_list_converter(self, afile):
        """Reads a file and returns a list based on the file contents"""
        
        alist = []
        '''
        try:
            for line in open(afile):
                separator = ','
                line = line.split(separator)
                for item in alist:
                    alist.append(item)
            return set(alist)
        except:
            raise IOError("File not found")
        '''
        file_ = open(afile, 'r')
        alist = file_.readlines()
        alist = [i.replace('\n','') for i in alist]
        return alist

    def room_picker(self, dict_):
        """Gets a random room with space"""
        pass

                   