class Room():
    """Class Room at Andela"""
    wants_accommodation = False
    def __init__(self, room_name):
        self.occupants = []
        self.room_name = room_name
       
        
class LivingSpace(Room):
    """Class LivingSpace inherits from Room"""
    capacity = 4
    def __init__(self, room_name):
        super().__init__(room_name)
        self.occupants = []
        
class Office(Room):
    """Class Office inherits from Room"""
    capacity = 6
    def __init__(self, room_name):
        super().__init__(room_name)
        self.occupants = []

