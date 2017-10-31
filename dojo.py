class Person():
    """Class person for general Person"""
    def __init__(self, reg_number, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.reg_number = reg_number
        self.salary = salary
    
    @property    
    def fullname(self):
        """Find full name format"""
        return '{} {}'.format(self.first_name, self.second_name)
    
    @property    
    def email(self):
        """Find email format"""
        return '{}.{}'.format(self.first_name.lower(), self.second_name.lower()) + '@' + 'andela.com'
        
class Fellow(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, reg_number, first_name, second_name, salary=40000, wants_accommodation=False):
        super().__init__(reg_number, first_name, second_name, salary)
        self.wants_accommodation = wants_accommodation
        
class Staff(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, reg_number, first_name, second_name, salary=70000):
        super().__init__(reg_number, first_name, second_name, salary)
        
class Room():
    """Class Room for people"""
    def __init__(self, room_number, occupants):
        self.occupants = occupants
        self.room_no = room_number
        
class LivingSpace(Room):
    """Class LivingSpace inherits from Room"""
    def __init__(self, room_number, occupants=4):
        super().__init__(room_number, occupants)
        
class Office(Room):
    """Class Office inherits from Room"""
    def __init__(self, room_number, occupants=6):
        super().__init__(room_number, occupants)
        
class Dojo(Person, Room):
    """Class Dojo inherits from both Person and Room"""
    def __init__(self, living_space):
        self.living_space = living_space
        
    '''
    def allocate_living_space(self):
        if isinstance(object, Fellow) and object.Fellow.wants_accommodation is True
                and LivingSpace.occupants < 6:
            #Give accommodation to fellow
            object.LivingSpace.occupants += 1
        
        else:
            print("Only fellows are allocated living spaces")
            '''   