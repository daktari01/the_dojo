from room import Room, Office, LivingSpace


class Dojo:
    """Class Dojo randomly allocates rooms"""
    def __init__(self):
        self.occupants = []
        self.rooms=[]
        
    def create_room(self, room_types, room_name):
        '''
        mapping = {'office': Office,'livingspace':LivingSpace}
        
        new_room = mapping[room_types](room_name)
        return new_room
        '''
        if room_types == 'office':
            new_room = Office(room_name)
            self.rooms.append(new_room.room_name)
        elif room_types == 'livingspace':
            new_room = LivingSpace(room_name)
        else:
            return "weklwelkwe;lek"
        return self.rooms