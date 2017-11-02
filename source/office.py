from room import Room


class Office(Room):
    """Class Office inherits from Room"""
    def __init__(self, room_number, occupants=6):
        super().__init__(room_number, occupants)