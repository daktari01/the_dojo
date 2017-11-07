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
