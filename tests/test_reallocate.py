import unittest

from src.dojo import Dojo


class ReallocateTest(unittest.TestCase):
    """Test the dojo module"""
    def setUp(self):
        self.dojo = Dojo()
        

    def test_check_which_room_person_is(self):
        """Tests the method that checks which room a person is"""
        dict_a = {
            'Mandela': ['David', 'Samuel', 'Turi'],
            'Machel':['Anne', 'Linet', 'Turi']
        }
        dict_b = {
            'Nyerere': ['Myles', 'Reginald', 'Booker'],
            'Obote':['Memo', 'Liliosa']
        }
        self.assertEqual(self.dojo.check_which_room_person_is('Liliosa',\
                                                             dict_b), 'Obote')
        self.assertEqual(self.dojo.check_which_room_person_is('Francis',\
                                                            dict_a), False)

    def test_reallocate_person_removes_person(self):
        """Tests that a person has indeed been reallocated a room"""
        self.dojo.create_room('office', 'Mandela')
        self.dojo.create_room('office', 'Madiba')
        self.dojo.add_person('Joseph Simiyu', 'staff')
        if self.dojo.room_is_empty('Mandela'):
            self.dojo.reallocate_person('Joseph Simiyu', 'Mandela')
            self.assertEqual(len(self.dojo.dict_offices['Mandela']), 1)
        else:
            self.dojo.reallocate_person('Joseph Simiyu', 'Madiba')
            self.assertEqual(len(self.dojo.dict_offices['Madiba']), 1)

    def test_room_is_empty(self):
        """Tests the room_is_empty function"""
        self.dojo.create_room('office', 'Sama')
        self.dojo.add_person('Linda Masero', 'staff')
        self.assertFalse(self.dojo.room_is_empty('Sama'))


