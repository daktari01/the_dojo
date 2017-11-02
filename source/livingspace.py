from room import Room


class LivingSpace(Room):
    """Class LivingSpace inherits from Room"""
    def __init__(self, room_number, occupants=4):
        super().__init__(room_number, occupants)