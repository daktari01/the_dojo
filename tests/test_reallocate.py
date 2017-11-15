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

    