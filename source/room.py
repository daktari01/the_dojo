import random

from source.person import Person, Staff, Fellow
from source.dojo import Dojo


class Room():
    """Class Room at Andela"""
    wants_accommodation = False
    def __init__(self, room_name):
        self.occupants = []
        self.room_name = room_name

    def get_occupants(self):
        """Return all occupants"""
        for occupant in self.occupants:
            print (occupant)

    def get_random_room(self, room_dict, room_capacity):
        """Returns a random room that has available space"""
        # Pick a random key from the dictionary
        random_key = random.choice(list(room_dict))

        while room_capacity == len(room_dict[random_key]):
            random_key = random.choice(list(room_dict))
        return random_key


        def allocate_office(self, person_name, person_type):
            """Allocates an office to a person"""
            # Get a random office that has space
            office_capacity = 6
            available_office = self.get_random_room(self.dict_offices, office_capacity)
            available_office.append(person_name)
            return available_office 
        
        
class LivingSpace(Room):
    """Class LivingSpace inherits from Room"""
    capacity = 4
    def __init__(self, room_name):
        super().__init__(room_name)
        self.occupants = []

    def get_room_type(self):
        return LivingSpace.__name__

    def is_full(self):
        if self.capacity == len(self.occupants):
            return True
        return False

        
class Office(Room):
    """Class Office inherits from Room"""
    capacity = 6
    def __init__(self, room_name):
        super().__init__(room_name)
        self.occupants = []

    def get_room_type(self):
        return Office.__name__

    def is_full(self):
        if self.capacity == len(self.occupants):
            return True
        return False
