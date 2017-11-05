import random

from source.person import Person, Staff, Fellow


class Room():
    """Class Room at Andela"""
    wants_accommodation = False
    def __init__(self, room_name):
        self.occupants = []
        self.room_name = room_name
        
    def get_random_room(self, random_room):
        """Method to get a random room"""
        pass

    def get_occupants(self):
        """Return all occupants"""
        for occupant in self.occupants:
            print (occupant)
        
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

    def allocate_to_person(self, fellow):
        if len(self.occupants) < self.capacity:
            if isinstance(fellow, Fellow) and self.wants_accommodation=='Y':
                self.occupants.append(fellow)
        return self.occupants
        
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

    def get_random_office(self):
        """Returns a random office to allocate to person"""
        

    def allocate_to_person(self, person):
        if len(self.occupants) < self.capacity:
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants