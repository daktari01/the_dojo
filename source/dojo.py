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
    
    def create_room(self, room_type, room_name):
        """Method to create rooms and allocate"""
        new_offices = []
        new_livings =[]
        if isinstance(room_type, str) and isinstance(room_name, str):
            if room_type.lower() == "office":
                for new_office in new_offices:
                    for office in self.all_offices:
                        if new_office == office:
                            print("Office already exists. Please try using a different name")
                        else:
                            self.all_offices.extend(new_offices)
            elif room_type.lower() == "living":
                for new_living in new_livings:
                    for living in self.all_livings:
                        if new_living == living:
                            print("Living space already exists. Please try using a different name")
                        else:
                            self.all_livings.extend(new_livings)


    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """Method to add person"""
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
            for line in open('./files/fellows.txt'):
                separator = ','
                line = line.split(separator)
                for fellow in line:
                    self.all_fellows.append(fellow)

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
            for line in open('./files/staff.txt'):
                separator = ','
                line = line.split(separator)
                for staff in line:
                    self.all_staff.append(staff)
            # Join the all_fellows and all_staff lists to obtain all_people list
            self.all_people = self.all_fellows.extend(self.all_staff)

        else:
            print("Wrong person type entered. Please try again")
        return self.all_people
       
    

             