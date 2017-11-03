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
    wants_accommodation = False
    def __init__(self, person_name):
        super().__init__(person_name)
    
    