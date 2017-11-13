import unittest
import io
import sys
import re

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from io import StringIO
from src.room import Room, Office, LivingSpace
from src.person import Person, Staff, Fellow
from src.dojo import Dojo


class DojoTest(unittest.TestCase):
    """Test the dojo module"""
    def setUp(self):
        self.dojo = Dojo()
        

    def test_default_want_accommodation_for_fellow(self):
        """Test default value for Fellow wants accommodation"""
        fellow2 = Fellow('Omingo')
        self.assertEqual('N', fellow2.wants_accommodation)

    def test_living_object_type(self):
        """Test the type of LivingSpace class object"""
        living3 = LivingSpace('room4')
        self.assertTrue(isinstance(living3, LivingSpace))

    def test_office_object_type(self):
        """Test the type of Office class object"""
        office3 = LivingSpace('room4')
        self.assertTrue(isinstance(office3, LivingSpace))
    
    def test_create_room_successfully(self):
        """Tests that a new room is successfully created"""
        initial_office_count = len(self.dojo.all_offices)
        self.dojo.create_room("office", "Turquoise")
        new_office_count = len(self.dojo.all_offices)
        self.assertEqual(new_office_count - initial_office_count, 1)
       
    def test_cannot_create_dup_office(self):
        """Tests that duplicate office cannot be added"""
        self.dojo.create_room("office", "Grey")
        self.dojo.create_room("office", "Grey")
        output = "Office Grey created successfullyOffice already exists."\
                                " Please try using a different name"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                    sys.stdout.getvalue()), output)

    def test_cannot_create_dup_livingspace(self):
        """Tests that duplicate living space cannot be added"""
        self.dojo.create_room("living", "Grey")
        self.dojo.create_room("living", "Grey")
        output = "Living space Grey created successfullyLiving space already exists."\
                                " Please try using a different name"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                    sys.stdout.getvalue()), output)

    def test_cannot_create_dup_fellow(self):
        """Tests that duplicate fellow cannot be added"""
        self.dojo.add_person("Peter Alask", "fellow")
        self.dojo.add_person("Peter Alask", "fellow")
        output = "Peter Alask has been added as a FellowThere is no available"\
            +" office to add Peter Alask. Create one firstFellow already exists!"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                    sys.stdout.getvalue()), output)

    def test_cannot_create_dup_staff(self):
        """Tests that duplicate staff cannot be added"""
        self.dojo.add_person("Pet Alaska", "staff")
        self.dojo.add_person("Pet Alaska", "staff")
        output = "Pet Alaska has been added as a StaffThere is no available "\
            +"office to add Pet Alaska. Create one firstStaff already exists!"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                    sys.stdout.getvalue()), output)
    
    def test_person_staff_or_fellow(self):
        """Tests that only staff or office is entered as the person type"""
        self.dojo.add_person('John Doe', 'officer')
        output = "Wrong person type entered. Please try again"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                                sys.stdout.getvalue()), output)

    def test_add_staff_without_available_office(self):
        """Tests what is printed when staff is added with no office"""
        self.dojo.add_person('John Doe', 'staff')
        output = "John Doe has been added as a Staff"\
            +"There is no available office to add John Doe. Create one first"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                                sys.stdout.getvalue()), output)

    def test_add_fellow_without_available_office(self):
        """Tests what is printed when fellow is added with no office"""
        self.dojo.add_person('John Doe', 'fellow')
        output = "John Doe has been added as a Fellow"\
            +"There is no available office to add John Doe. Create one first"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                                sys.stdout.getvalue()), output)

    def test_add_fellow_without_available_living(self):
        """Tests what is printed when fellow is added with no living space"""
        self.dojo.add_person('Jane Doe', 'fellow', 'Y')
        output = "Jane Doe has been added as a FellowThere is no available"\
            +" office to add Jane Doe. Create one firstThere is no available "\
            +"living space to add Jane Doe. Create one first"
        self.assertEqual(re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~][\n]*', '', \
                                                sys.stdout.getvalue()), output)
   

if __name__ == '__main__':
    unittest.main(exit=False)