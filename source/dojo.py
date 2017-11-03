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
            for room_name in self.all_rooms:
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
        if person_type == 'FELLOW' and wants_accommodation == 'N':
            new_person = Fellow(person_name)
            self.all_people.append(person_name.self.person_name)
            self.all_fellows.append(person_name.self.person_name)
        elif person_type == 'FELLOW' and wants_accommodation == 'Y':
            new_person = Fellow(person_name, 'Y')
            self.all_people.append(person_name.self.person_name)
        elif person_type == 'STAFF':
            new_person = Staff(person_name)
            self.all_people.append(person_name.self.person_name)
        return self.all_people
       
    
          