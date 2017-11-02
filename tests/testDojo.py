import unittest

from ..source.person import Person
from ..source.fellow import Fellow
from ..source.staff import Staff
from ..source.room import Room
from ..source.livingspace import LivingSpace
from ..source.office import Office
from ..source.dojo import Dojo


class DojoTest(unittest.TestCase):
    """Test the dojo module"""
    
    def test_person_instance(self):
        """Test instance of class Person"""
        person1 = Person(12, 'Kioko', 'Mwau', 30000)
        self.assertIsInstance(person1, Person)
        
    def test_fellow_instance(self):
        """Test instance of class Fellow"""
        fellow1 = Fellow(15, 'Kazungu', 'Dede', True)
        self.assertIsInstance(fellow1, Fellow)
        
    def test_staff_instance(self):
        """Test instance of class Staff"""
        staff1 = Staff(17, 'Chepngetich', 'Jelimo')
        self.assertIsInstance(staff1, Staff)
        
    def test_room_instance(self):
        """Test instance of class Room"""
        room1 = Room(26, 3)
        self.assertIsInstance(room1, Room)
        
    def test_livingspace_instance(self):
        """Test instance of class LivingSpace"""
        living1 = LivingSpace(24)
        self.assertIsInstance(living1, LivingSpace)
        
    def test_office_instance(self):
        """Test instance of class Office"""
        office1 = Office(25)
        self.assertIsInstance(office1, Office)

    def test_person_fullname(self):
        """Test full name format of class Person"""
        person4 = Person(11, 'Omuse', 'Ekirapa', 45000)
        self.assertEqual(person4.fullname, 'Omuse Ekirapa')

    def test_person_email(self):
        """Test email format of class Person"""
        person2 = Person(19, 'Nkirote', 'Vaite', 30000)
        self.assertEqual(person2.email, 'nkirote.vaite@andela.com')

    def test_default_want_accommodation_for_fellow(self):
        """Test default value for Fellow wants accommodation"""
        fellow2 = Fellow(4, 'Omingo', 'Moseti')
        self.assertEqual(False, fellow2.wants_accommodation)

    def test_object_type(self):
        """Test the type of class object"""
        living3 = LivingSpace(32)
        self.assertTrue(type(living3) is LivingSpace)


if __name__ == '__main__':
    unittest.main(exit=False)