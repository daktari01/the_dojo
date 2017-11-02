from room import Room
from fellow import Fellow


class LivingSpace(Room):
    """Class LivingSpace inherits from Room"""
    capacity = 4
    def __init__(self, room_number):
        super().__init__(room_number)
        self.occupants = []

    def get_room_type(self):
        return LivingSpace.__name__

    def is_full(self):
        if self.capacity == len(self.occupants):
            return True
        return False

    def allocate_to_person(self, fellow):
        if len(self.occupants) < self.capacity:
            if isinstance(fellow, Fellow) and self.wants_accommodation==True:
                self.occupants.append(fellow)
        return self.occupants