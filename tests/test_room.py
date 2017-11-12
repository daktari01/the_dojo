import unittest

from src.room import Room, Office, LivingSpace

class TestRoom(unittest.TestCase):
    """Tests the room module"""
    def test_room_instance(self):
        """Test instance of class Room"""
        room1 = Room('room1')
        self.assertIsInstance(room1, Room)
        
    def test_livingspace_instance(self):
        """Test instance of class LivingSpace"""
        living1 = LivingSpace('livingroom3')
        self.assertIsInstance(living1, LivingSpace)
        
    def test_office_instance(self):
        """Test instance of class Office"""
        office1 = Office('Mandela')
        self.assertIsInstance(office1, Office)

if __name__ == '__main__':
    unittest.main(exit=False)