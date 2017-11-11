import unittest
import io
import sys
import re

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from io import StringIO
from source.room import Room, Office, LivingSpace
from source.person import Person, Staff, Fellow
from source.dojo import Dojo


class DojoTest(unittest.TestCase):
    """Test the dojo module"""
    def setUp(self):
        self.dojo = Dojo()
        
    def test_person_instance(self):
        """Test instance of class Person"""
        person1 = Person('Kioko')
        self.assertIsInstance(person1, Person)
        
    def test_fellow_instance(self):
        """Test instance of class Fellow"""
        fellow1 = Fellow('Kazungu', 'Y')
        self.assertIsInstance(fellow1, Fellow)
        
    def test_staff_instance(self):
        """Test instance of class Staff"""
        staff1 = Staff('Chepngetich')
        self.assertIsInstance(staff1, Staff)
        
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

    def test_default_want_accommodation_for_fellow(self):
        """Test default value for Fellow wants accommodation"""
        fellow2 = Fellow('Omingo')
        self.assertEqual('N', fellow2.wants_accommodation)

    def test_object_type(self):
        """Test the type of class object"""
        living3 = LivingSpace('room4')
        self.assertTrue(isinstance(living3, LivingSpace))
    
    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.all_offices)
        blue_office = self.dojo.create_room("office", "Turquoise")
        new_room_count = len(self.dojo.all_offices)
        self.assertEqual(new_room_count - initial_room_count, 1)
       
    def test_cannot_create_office(self):
        blue_office = self.dojo.create_room("office", "Grey")
        blue_office_dup = self.dojo.create_room("office", "Grey")
        output = "Office Grey created successfullyOffice already exists. Please try using a different name"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                    sys.stdout.getvalue()), output)
    
    def test_person_staff_or_fellow(self):
        person1 = self.dojo.add_person('John Doe', 'officer')
        output = "Wrong person type entered. Please try again"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                                sys.stdout.getvalue()), output)

    
   

if __name__ == '__main__':
    unittest.main(exit=False)