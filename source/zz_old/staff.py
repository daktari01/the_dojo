from person import Person


class Staff(Person):
    """Class Fellow inheriting from Person"""
    def __init__(self, name):
        super().__init__(name)