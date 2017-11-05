from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow


class Dojo:
    """All functionality is implemented here"""
    path = './files/'
    def __init__(self):
        self.occupants = []
        self.all_rooms = {}
        self.rooms =[]
        self.all_people = []
        self.all_staff = []
        self.all_fellows = []
        self.all_offices = {}
        self.offices = []

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
            for line in open('fellows.txt'):
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
            for line in open('staff.txt'):
                separator = ','
                line = line.split(separator)
                for staff in line:
                    self.all_staff.append(staff)
            # Join the all_fellows and all_staff lists to obtain all_people list
            self.all_people = self.all_fellows.extend(self.all_staff)
            
        else:
            raise RuntimeError("Wrong person type entered. Please try again")
        return self.all_people
          
    def create_room(self, room_types, room_name):
        """Method to create rooms"""
        if isinstance(room_types, str) and isinstance(room_name, str):
            
            if room_types in self.all_rooms:
                print("Room name already exits!. Try another one")
            else:
                if room_types.lower() == 'office':
                    new_room = Office(room_name)
                    self.all_offices.update({room_name:self.rooms})
                    #self.all_rooms.append(new_room.room_name)
                    '''
                elif room_types.lower() == 'livingspace':
                    new_room = LivingSpace(room_name)
                else:
                    return "Invalid argument passed"
                return self.all_rooms
        else:
            raise TypeError("Only strings are allowed")
    '''

        
       
    
          