class Person():
    """Class person for general Person"""
    def __init__(self, person_name):
        self.person_name = person_name
        
class Staff(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, person_name):
        super().__init__(person_name)
        
class Fellow(Person):
    """Class Fellow inheriting from Person"""
    
    def __init__(self, person_name, wants_accommodation = 'N'):
        super().__init__(person_name)
        self.wants_accommodation = wants_accommodation
    
#jambo = Person("Mutai")
    