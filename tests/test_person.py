import unittest

from src.person import Person, Fellow, Staff


class TestPerson(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main(exit=False)