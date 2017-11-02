class Room():
    """Class Room at Andela"""
    def __init__(self, room_name):
        self.occupants = []
        self.room_name = room_name

    def get_occupants(self):
        """Return the number of occupants"""
        return self.occupants