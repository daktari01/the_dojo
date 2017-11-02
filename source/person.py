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