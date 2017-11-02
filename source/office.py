from room import Room
from staff import Staff
from fellow import Fellow


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

    def allocate_to_person(self, person):
        if len(self.occupants) < self.capacity:
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants



