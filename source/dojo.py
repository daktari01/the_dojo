from room import Room, Office, LivingSpace
from person import Person, Staff, Fellow


class Dojo:
    """Class Dojo randomly allocates rooms"""
    def __init__(self):
        self.occupants = []
        self.all_rooms = []
        self.all_people = []
        self.all_staff = []
        self.all_fellows = []
        
    def create_room(self, room_types, room_name):
        """Method to create rooms"""
        if isinstance(room_types, str) and isinstance(room_name, str):
            if room_name in self.all_rooms:
                print("Room name already exits!. Try another one")
            else:
                if room_types.lower() == 'office':
                    new_room = Office(room_name)
                    self.all_rooms.append(new_room.room_name)
                elif room_types.lower() == 'livingspace':
                    new_room = LivingSpace(room_name)
                else:
                    return "Invalid argument passed"
                return self.all_rooms
        else:
            raise TypeError("Only strings are allowed")
    
    def add_person(self, person_name, person_type, wants_accommodation='N'):
        # person_name = args['<person_name>']
        # person_type = args['<person_type>']
        
        if person_type.upper() == 'FELLOW':
            for fellow in self.all_fellows:
                if fellow == person_name:
                    print("Fellow already exists!")
                    return
            new_person = Fellow(person_name)
            self.all_fellows.append(new_person)
            self.all_people.append(new_person)
        elif person_type.upper() == 'STAFF':
            for staff in self.all_staff:
                if staff == person_name:
                    print("Staff already exists!")
                    return
            new_person = Staff(person_name)
            self.all_staff.append(new_person)
            self.all_people.append(new_person)
        else:
            raise RuntimeError("Wrong person type entered. Please try again")
        return self.all_people
        
       
    
          